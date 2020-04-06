from django.urls import path
from . import views
#from .views import CityListView

urlpatterns = [
   path('', views.index, name='home'),
   #path('', CityListView.as_view(), name='home'),
   path('delete/<city_name>/', views.delete_city, name='delete_city'),
]