from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.core.mail import send_mail
from .models import Contato, EmailNewsletter

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def faqs(request):
    return render(request, 'faqs.html')

def contato(request):
    return render(request, 'contato.html')

def analise_empresa(request):
    return render(request, 'analise_empresa.html')

def gestao_trafego(request):
    return render(request, 'gestao_trafego.html')

def identidade_visual(request):
    return render(request, 'identidade_visual.html')

def criativos(request):
    return render(request, 'criativos.html')

def desenvolvimento_web(request):
    return render(request, 'desenvolvimento_web.html')

def posts(request):
    return render(request, 'posts.html')



def mensagem(request):
    """Recebe nova mensagem"""
    if request.method == 'POST':
        novo_contato = Contato()
        novo_contato.nome = request.POST['nome']
        novo_contato.email = request.POST['email']
        novo_contato.empresa = request.POST['empresa']
        novo_contato.save()
        #send_mail('Novo email no site!', 'Novo email de ' + novo_contato.nome + ' no site', 'fodase@fodase.com', ['guibaaa@gmail.com'], fail_silently=False)
        return HttpResponse('Aguarde nosso contato!')
    else:
        return HttpResponse('Erro ao enviar mensagem!')

def emailNewsletter(request):
    """Recebe cadastro na newsletter"""
    if request.method == 'POST':
        novo_email = EmailNewsletter()
        novo_email.email = request.POST['email']
        novo_email.save()
        return HttpResponse('Cadastrado com sucesso!')
    else:
        return HttpResponse('Erro ao cadastrar!')