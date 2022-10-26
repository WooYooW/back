from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('delete/', views.delete, name='delete'),
    path('signup/', views.signup, name='signup'),
    path('update/', views.update, name='update'),
    path('<int:pk>/detail', views.detail, name='detail'),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path('password/', views.change_password, name='change_password'),
    path('', views.index, name="index"),
]

