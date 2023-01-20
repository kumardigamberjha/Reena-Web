from django.urls import path, include

from Booking import views

urlpatterns = [
    path('', views.AddBookingView, name="add_booking"),
    path('ProductCat/', views.AddProductCat, name="add_product_cat"),

    path('Product/', views.AddProductView, name="add_product_view"),
    path('ProductAccounts/', views.Accounts, name="prodaccounts"),

    path('Get_booking_data/', views.GetBookingPrice, name='get_booking_price'),
    path('Get_booking_datentime/', views.GetBookingDatentime, name='get_booking_datentime'),

    path("Show_Booking/", views.ShowBookingModel, name="show_booking"),
    path("Show_Products/", views.ShowProductModel, name="show_product_model"),

    path("View_BookingData/<int:id>/", views.ViewBookingModelData, name="view_booking_data"),

    path("Update_ProductCat/<int:id>/", views.UpdateProductCat, name="update_prod_cat"),
    path("Update_Product/<int:id>/", views.UpdateProductView, name="update_prod_view"),

]