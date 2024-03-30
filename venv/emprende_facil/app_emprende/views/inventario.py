from django.shortcuts import render

def inventario(request):
    return render(request, "app_emprende/inventario.html")