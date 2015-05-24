from django.db import models

# Create your models here.

class Visitor(models.Model):
    """ユーザ"""
    name = models.CharField(u'ユーザ名', max_length=255)
    nfc_id = models.CharField(u'nfcID', max_length=255)

    def __str__(self):
        return self.name

class Log(models.Model):
    """訪問ログ"""
    visitor = models.ForeignKey(Visitor, verbose_name=u'ユーザ', related_name='logs')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.id
