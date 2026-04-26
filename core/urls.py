from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('tumb/<int:id>/', views.tumb_detail, name='tumb_detail'),
    path('categories/', views.get_categories, name='categories'),
    path('categories/<int:category_id>/', views.get_category, name='category'),
    path('about/', views.about),
    path('favorite/<int:id>/', views.add_favorite, name='add_favorite'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)