"""Reena URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Reena.views import Login_view, Logout_view, Signup_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('Booking/', include('Booking.urls')),
    # path(r'^paypal/', include('paypal.standard.ipn.urls')),

    path('login/', Login_view, name="login"),
    path('logout/', Logout_view, name="logout"),
    path('SignUp/', Signup_view, name="signup"),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)