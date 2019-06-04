from django.urls import path, re_path
from level_2_app import views

urlpatterns = [
    re_path(r'^$',views.index,name='index')
]
