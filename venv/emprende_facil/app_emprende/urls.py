from django.urls import path
## para añadir otra url, utilisa:
##from views.modulo. importar funcion 
from .views import index
from .views import inventario
from .views import area_trabajo


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path("", index.index, name="index"),
    path("inventario", inventario.inventario, name="inventario"),
    path("area_trabajo", area_trabajo.area_trabajo, name="area_trabajo"),
    path('delete_product/<int:product_id>/', area_trabajo.delete_product, name='delete_product'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)