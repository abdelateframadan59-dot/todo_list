from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<str:pk>/', views.Updatetask, name='update'),
    path('delete/<str:pk>/', views.deletetask, name='delete'),
    

    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='todo/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),]
    