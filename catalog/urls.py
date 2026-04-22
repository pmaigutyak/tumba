from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tumb/<int:id>/', views.tumb_detail, name='tumb_detail'),
    path('categories/', views.get_categories, name='categories'),
    path('about/',views.about )
]