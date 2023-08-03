from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('last3/', views.home, name='home'),
    path('', views.kunstverzeichnis, name='kunstverzeichnis'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('search/', views.search, name='search'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # New
