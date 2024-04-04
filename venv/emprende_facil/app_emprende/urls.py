from django.urls import path
## para añadir otra url, utilisa:
##from views.modulo. importar funcion 
from .views import index
from .views import edu
from .views import area_trabajo
from .views import user_log
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path("", index.index, name="index"), 
    path('updateLevel', index.update_level, name='update_level'),
    path('get-level/', index.get_level, name='get_level'),
    path("ventas", edu.ventas, name="ventas"),
    path("inventario", edu.inventario, name="inventario"),
    path("area_trabajo", area_trabajo.area_trabajo, name="area_trabajo"),
    path('delete_product/<int:product_id>/', area_trabajo.delete_product, name='delete_product'),
    path('signup/', user_log.signup, name='signup'),
    path('login/', user_log.user_login, name='login'),
    path('logout/', user_log.user_logout, name='logout'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)