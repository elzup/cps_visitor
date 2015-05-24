# -*- coding: utf-8 -*-
from django.forms import ModelForm
from cms.models import Visitor, Log


class VisitorForm(ModelForm):
    """訪問者のフォーム"""
    class Meta:
        model = Visitor
        fields = "__all__"

class LogForm(ModelForm):
    """ログのフォーム"""
    class Meta:
        model = Log
        fields = "__all__"
