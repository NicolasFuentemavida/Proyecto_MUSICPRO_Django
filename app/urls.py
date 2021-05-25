from django.urls import path
from .views import donaciones, index, productos, contacto

urlpatterns = [
    path('', index, name="index"),
    path('productos/', productos, name="productos"),
    path('contacto/', contacto, name="contacto"),
    path('donaciones/', donaciones, name="donaciones"),
]