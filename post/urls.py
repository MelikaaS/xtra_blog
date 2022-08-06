from django.urls import path
from . import views

app_name='post'
urlpatterns=[
    path('post/<slug:slug>',views.post,name='post_app')
    # path('side', views.sidebar, name="side")
]


# <int:id>
# <str:title>