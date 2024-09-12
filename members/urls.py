from django.urls import path
from members import views

urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('create/', views.member_create, name='member_create'),
    path('<int:id>/edit/', views.member_update, name='member_update'),
    path('<int:id>/delete/', views.member_delete, name='member_delete'),
]
