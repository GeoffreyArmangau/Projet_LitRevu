from django.urls import path
from . import views

urlpatterns = [
    path('flux/', views.flux, name='flux'),
    path('flux/data/', views.flux_data, name='flux_data'),
    path('ticket/create/', views.create_ticket, name='create_ticket'),
]
