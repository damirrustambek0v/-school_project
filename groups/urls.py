from django.urls import path
from .import views

app_name = 'groups'

urlpatterns = [
    path('list/', views.group_list, name='list'),
    path('form/',views.group_form, name='form'),
    path('detail/<int:pk>/', views.group_detail, name='detail'),
    path('delete/<int:pk>/',views.group_delete, name='delete'),

]
