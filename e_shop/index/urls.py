from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.picture_list, name='picture_list'),
    path('like/<int:picture_id>/', views.like_picture, name='like_picture'),
    path('comment/<int:picture_id>/', views.add_comment, name='add_comment'),
]
