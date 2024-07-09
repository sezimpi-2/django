from django.contrib import admin
from django.urls import path
from news_blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('text/', views.text_response_view, name='text_response'),
    path('objects/', views.model_objects_view, name='model_objects'),
    path('template/', views.template_view, name='template_view'),
    path('', views.template_view, name='home'),  # главная страница
]