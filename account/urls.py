from django.urls import path
from authentication import views
from django.views.decorators.http import require_POST
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('profil/', views.profil, name='profil'),
    path('logout/', views.logout_user, name='logout'),
    path('modif/', views.modif, name='modif')
    
]