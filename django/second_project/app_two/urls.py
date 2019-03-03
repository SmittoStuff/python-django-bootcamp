from django.urls import path, re_path
from app_two import views

urlpatterns = [
    re_path(r'^$',views.help,name='help'),
]
