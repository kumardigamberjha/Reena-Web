from django.urls import path
from Pages import views

urlpatterns = [
    path('', views.EditPageView, name="editpage"),
    path('HomePage/', views.HomePageView, name="homepage"),
    path('AboutPage/', views.AboutusPageView, name="aboutpage"),
]