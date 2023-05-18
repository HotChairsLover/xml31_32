from django.urls import path
from . import views

urlpatterns = [
    path('', views.GenPdf.as_view(), name="pdfgen"),
]
