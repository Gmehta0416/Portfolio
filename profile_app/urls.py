from django.urls import path,include
from profile_app import views
urlpatterns = [
    path('',views.Home,name="home"),
    path('blog/',views.Blog,name="blog"),
]
