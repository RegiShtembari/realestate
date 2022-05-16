from unicodedata import name
from django.urls import path

from . import views

app_name = 'pronat'

urlpatterns = [
    path('', views.properties_all, name="home_page"),
    path('properties', views.properties_list, name="properties_list"),
    path('property/<slug:slug>', views.property_detail, name = "property_detail"),
    path('apartment', views.apartment_all, name="apartment_all"),
    path('land', views.land_all, name="land_all"),
    path('garage', views.garage_all, name="garage_all"),
    path('store', views.store_all, name="store_all"),
    path('villa', views.villa_all, name="villa_all"),
    path('contact', views.contact_page,name="contact_page"),
    path('about',views.aboutus,name="aboutus"),
    path('politikat',views.politikat_privatesise,name="politkat"),
<<<<<<< Updated upstream
    # path('prova',views.provaa,name="prova"),
=======
    #path('prova',views.provaa,name="prova"),
>>>>>>> Stashed changes
]