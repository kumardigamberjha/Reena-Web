from django.urls import path, include

from Booking import views

urlpatterns = [
    path('', views.AddBookingView, name="add_booking"),
    path('ProductCat/', views.AddProductCat, name="add_product_cat"),
    path('Product/', views.AddProductView, name="add_product_view"),

    path("select2/", include("django_select2.urls")),


    path('Get_booking_data/', views.GetBookingPrice, name='get_booking_price'),
    path('Get_booking_datentime/', views.GetBookingDatentime, name='get_booking_datentime'),

    path("Show_Booking/", views.ShowBookingModel, name="show_booking"),
    path("View_BookingData/<int:id>/", views.ViewBookingModelData, name="view_booking_data")
]