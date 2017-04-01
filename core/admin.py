from django.contrib import admin
from django.http.request import HttpRequest
from django.utils.html import format_html, mark_safe

from .models import Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    fields = ('label', 'uid', 'url', 'custom_id', 'user', 'get_link')
    list_display = ('label', 'url', 'get_link')
    list_filter = ('url',)
    list_display_links = ('label',)
    readonly_fields = ('uid', 'get_link')
    search_fields = ('label', 'url')

    def get_link(self, obj):
        return format_html("<a href={}>{}</a>", mark_safe(obj.url), obj.url)
    get_link.short_description = 'Link'
