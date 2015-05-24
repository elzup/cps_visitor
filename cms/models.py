from django.db import models

# Create your models here.

class Visitor(models.Model):
    """ユーザ"""
    name = models.CharField(u'ユーザ名', max_length=64)
    full_name = models.CharField(u'本名', max_length=64, default=None)
    univ_id = models.CharField(u'学籍番号', max_length=64, default=None)
    nfc_id = models.CharField(u'nfcID', max_length=64, default=None)

    def __str__(self):
        return self.name

class Log(models.Model):
    """訪問ログ"""
    visitor = models.ForeignKey(Visitor, verbose_name=u'ユーザ', related_name='logs')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.id
