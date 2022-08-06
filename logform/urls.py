from django.urls import path
from . import views

app_name='input'
urlpatterns=[
    # path('logform/',views.signin, name='logform'),
    path('logform/',views.login_view, name='logform'),
    path('logform',views.signout,name='logout'),
    path('log', views.signup, name='signup'),
    path('edit/',views.edit_user, name="edit")
]