from user_info import views
from django.urls import path

app_name = 'user_info'

urlpatterns = [
    path('home/', views.home, name='home'),

]
