from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.db import transaction
from .forms import ProductoForm, ClienteForm, VentaForm
from ..models import Producto, Cliente, Venta, VentaDetalle
from django.db.models import Sum

def area_trabajo(request):
    context = {}
    
    if request.method == 'POST':
        form_productos = ProductoForm(request.POST)
        form_cliente = ClienteForm(request.POST)
        form_venta = VentaForm(request.POST)
        
        if form_productos.is_valid():
            form_productos.save()
            return redirect('area_trabajo')

        if form_cliente.is_valid():
            form_cliente.save()
            return redirect('area_trabajo')
       
        if form_venta.is_valid():
            venta = form_venta.save()
            # Calcular el total de la venta
            total_venta = VentaDetalle.objects.filter(venta=venta).aggregate(total_venta=Sum('total'))['total_venta']
            if not total_venta:
                total_venta = 0
            # Agregar el total al contexto
            context['total_venta'] = total_venta
            return redirect('area_trabajo')

    else:
        form_productos = ProductoForm()
        form_cliente = ClienteForm()
        form_venta = VentaForm()

    context.update({
        "form_productos": form_productos,
        "form_cliente": form_cliente,
        "form_venta": form_venta,
        "productos": Producto.objects.all(),
        "clientes": Cliente.objects.all(),
        "ventas": Venta.objects.all(),
    })
    return render(request, 'app_emprende/area_trabajo.html', context)
def delete_product(request, product_id):
    # Eliminar un producto específico
    product = get_object_or_404(Producto, pk=product_id)
    if request.method == 'POST':
        product.delete()
    return redirect('area_trabajo')  # Redirigir a la página principal o a la lista de productos