from django.urls import path
from . import views

app_name = 'firstapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('classify/<str:filename>', views.classify, name='classify'),
    path('upload/', views.upload, name='upload')
]