from django.urls import path,include
from profile_app import views
urlpatterns = [
    path('',views.profile,name="profile"),
]
