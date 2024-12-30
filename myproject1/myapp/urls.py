from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
    path('login/', views.login_view, name='login'),
]
