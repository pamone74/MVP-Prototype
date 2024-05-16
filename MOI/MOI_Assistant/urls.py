from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('assistant/', views.MOI_Assistant, name='MOI_Assistant'),
    path('chat/', views.chat_view, name='chat_view'),
    path('base/', views.base, name='base'),
    path('statistics/', views.statistics, name='statistics'),
    path('payment/', views.payment, name='payments'),
    path('gamified/', views.gamified, name='Gamified'),
]
