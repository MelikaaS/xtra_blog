from django.urls import path
from . import views

app_name='home'
urlpatterns=[
    path('', views.home,name='home_app'),
    path('search_eng',views.search,name='search_eng')
]