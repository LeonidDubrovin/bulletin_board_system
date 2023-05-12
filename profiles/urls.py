from django.urls import path

from .import views

urlpatterns = [
    path('my-ads/', views.profile_ads, name='my-ads'),
    path('profile-settings/', views.profile_settings, name='profile-settings'),
]
