from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),
    path('faqs', views.faqs, name='faqs'),
    path('contato', views.contato, name='contato'),
    path('analise_empresa', views.analise_empresa, name='analise_empresa'),
    path('gestao_trafego', views.gestao_trafego, name='gestao_trafego'),
    path('identidade_visual', views.identidade_visual, name='identidade_visual'),
    path('criativos', views.criativos, name='criativos'),
    path('desenvolvimento_web', views.desenvolvimento_web, name='desenvolvimento_web'),
    path('posts', views.posts, name='posts'),
    path('mensagem/', views.mensagem, name='mensagem'),
    path('email_newsletter/', views.emailNewsletter, name='email_newsletter'),
]