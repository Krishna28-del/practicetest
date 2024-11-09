from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.personal_details, name='personal_details'),
    path('portfolio/', views.portfolio, name='portfolio'),
]