from django.contrib import admin
from .models import Contato, EmailNewsletter

class ListandoContatos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'empresa', 'data', 'respondida')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'empresa')
    list_filter = ('respondida', 'data', 'empresa',)
    list_editable = ('respondida',)
    list_per_page = 10

class ListandoEmails(admin.ModelAdmin):
    list_display = ('id', 'email', 'data', 'ativo',)
    list_display_links = ('id', 'email',)
    search_fields = ('email', 'data',)
    list_filter = ('ativo', 'data',)
    list_editable = ('ativo',)
    list_per_page = 10

admin.site.register(Contato, ListandoContatos)
admin.site.register(EmailNewsletter, ListandoEmails)