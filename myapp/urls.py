from django.urls import path
from myapp import views

app_name="myapp"

urlpatterns = [
    path('',views.index,name="home"),
    path('register/',views.register,name="register"),
    path('cast_vote/',views.cast_vote,name="cast_vote"),
    path('login/',views.login,name="login"),
]
