from django.shortcuts import render
from .forms import ProductoForm
from django.shortcuts import redirect
from ..models import Producto
from django.shortcuts import get_object_or_404

def area_trabajo(request):
    ##definicion de objetos
    
    productos = Producto.objects.all()

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Página a la que redirigir después de guardar el formulario
    else:
        form = ProductoForm()

    context = {
        "form": form,
        "productos":productos,
      
    }
    return render(request, 'app_emprende/area_trabajo.html', context)

def delete_product(request, product_id):
    product = get_object_or_404(Producto, pk=product_id)
    if request.method == 'POST':
        product.delete()
    return redirect('app_emprende/area_trabajo.html')  # Redirect to the product list page after deletion

