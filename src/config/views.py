from django.shortcuts import render


def mi_pagina_inicio(request):
    contexto = {}
    return render(request,'mi_pagina_inicio.html', contexto)



def login (request):
    if request.method == "POST":
        username = request.POST.get('username', default = None)
        password = request.POST.get('password', default = None)
    return render(request,'login.html', {})