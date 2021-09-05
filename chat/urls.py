from django.urls import path
from .import views
urlpatterns = [
    path('chat',views.chat,name="index"),
    path('get',views.get,name="try"),
    path("signup/",views.signup,name='signup'),
    path('',views.Login,name="login"),
    path("logout/",views.Logout),
   
]