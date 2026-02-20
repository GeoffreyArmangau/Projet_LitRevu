from django.urls import path
from . import views

urlpatterns = [
	path('review/create/', views.create_review, name='create_review'),
	path('review/answer/<int:ticket_id>/', views.create_review_answer, name='create_review_answer'),
]
