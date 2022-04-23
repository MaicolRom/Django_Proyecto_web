from django.contrib import admin
from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('personas/', views.lista_personas, name='lista_personas'),
    path('carga_personas/', views.carga_personas, name='carga_personas'),
    path('admin/', admin.site.urls),  
    path('create_folder/',views.create_folder),
    path('folder/',views.folder),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)