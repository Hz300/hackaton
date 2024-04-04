from django.shortcuts import render

def inventario(request):
    return render(request, "app_emprende/inventario.html")

def ventas(request):
    return render(request, "app_emprende/ventas.html")

def clientes(request):
    return render(request, "app_emprende/clientes.html")