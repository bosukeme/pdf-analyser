from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_pdf, name='upload_pdf'),
    path('display/<str:email>/', views.display_data, name='display_data'),
]
