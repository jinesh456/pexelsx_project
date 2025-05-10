from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
urlpatterns = [
    path('like/<int:photo_id>/', views.like_photo, name='like_photo'),
]
urlpatterns = [
    path('search/', views.search, name='search'),
]
urlpatterns = [
    path('upload/', views.upload_photo, name='upload_photo'),
]
urlpatterns = [
    path('signup/', views.signup, name='signup'),
]

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_photo, name='upload_photo'),
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('search/', views.search_view, name='search'),
]
