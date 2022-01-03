from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello, {}, de {} anos de idade!</h1>'.format(nome, idade))

def soma(request, a, b):
    soma = float(a) + float(b)
    return HttpResponse('A soma de {} e {} é igual a {}'.format(a, b, soma))

def subtracao(request, a, b):
    sub = float(a) - float(b)
    return HttpResponse('A diferença entre {} e {} é igual a {}'.format(a, b, sub))

def multiplicacao(request, a, b):
    mult = float(a) * float(b)
    return HttpResponse('O produto de {} e {} é igual a {}'.format(a, b, mult))

def divisao(request, a, b):
    div = float(a) / float(b)
    return HttpResponse('A divisão de {} por {} é igual a {}'.format(a, b, div))