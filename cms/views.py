# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.views.generic.list import ListView

from cms.forms import VisitorForm, LogForm
from cms.models import Visitor, Log


def visitor_list(request):
    """の一覧"""
    # return HttpResponse(u'訪問者の一覧')
    visitors = Visitor.objects.all().order_by('id')
    return render_to_response('cms/visitor_list.html',
                              {'visitors': visitors},
                              context_instance=RequestContext(request))


def visitor_edit(request, visitor_id=None):
    """訪問者の編集"""
    if visitor_id:
        visitor = get_object_or_404(Visitor, pk=visitor_id)
    else:
        visitor = Visitor()

    if request.method == 'POST':
        form = VisitorForm(request.POST, instance=visitor)
        if form.is_valid():
            visitor.save()
            return redirect('cms:visitor_list')
    else:
        form = VisitorForm(instance=visitor)

    return render_to_response('cms/visitor_edit.html',
                              dict(form=form, visitor_id=visitor_id),
                              context_instance=RequestContext(request))


def visitor_del(request, visitor_id):
    """訪問者の削除"""
    visitor = get_object_or_404(Visitor, pk=visitor_id)
    visitor.delete()
    return redirect('cms:visitor_list')


def log_edit(request, visitor_id, log_id=None):
    """ログの編集"""
    visitor = get_object_or_404(Visitor, pk=visitor_id)  # 親の訪問者を読む
    if log_id:  # log_id が指定されている (修正時)
        log = get_object_or_404(Log, pk=log_id)
    else:  # log_id が指定されていない (追加時)
        log = Log()

    if request.method == 'POST':
        form = LogForm(request.POST, instance=log)  # POST された request データからフォームを作成
        if form.is_valid():  # フォームのバリデーション
            log = form.save(commit=False)
            log.visitor = visitor  # このログの、親の訪問者をセット
            log.save()
            return redirect('cms:log_list', visitor_id=visitor_id)
    else:  # GET の時
        form = LogForm(instance=log)  # log インスタンスからフォームを作成

    return render_to_response('cms/log_edit.html',
                              dict(form=form, visitor_id=visitor_id, log_id=log_id),
                              context_instance=RequestContext(request))


def log_del(request, visitor_id, log_id):
    """ログの削除"""
    log = get_object_or_404(Log, log_id=log_id)
    log.delete()
    return redirect('cms:log_list', visitor_id=visitor_id)


class LogList(ListView):
    """ログの一覧"""
    context_object_name = 'logs'
    template_name = 'cms/log_list.html.html'
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        visitor = get_object_or_404(Visitor, pk=kwargs['visitor_id'])
        logs = visitor.logs.all().order_by('id')
        self.object_list = logs

        context = self.get_context_data(object_list=self.object_list, visitor=visitor)
        return self.render_to_response(context)
