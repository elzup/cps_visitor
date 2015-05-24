from django.contrib import admin
from cms.models import Visitor, Log

class VisitorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name',)
admin.site.register(Visitor, VisitorAdmin)

class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
    list_display_links = ('id', 'created_at',)
admin.site.register(Log, LogAdmin)
