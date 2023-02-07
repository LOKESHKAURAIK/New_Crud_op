from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('addemp', views.addemp),
    path('delete', views.delete),
    path('del', views.delt),
    path('update', views.update),
    path('search', views.search),


]
