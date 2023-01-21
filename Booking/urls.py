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

    path("Today_Booking/", views.TodayBooking, name="today_booking"),
    path("Today_Appointment/", views.TodayAppointment, name="today_appointment"),


    path("Show_Products/", views.ShowProductModel, name="show_product_model"),
    path("Show_Products_Category/", views.ShowProductCategoryModel, name="show_product_cat_model"),


    path("View_BookingData/<int:id>/", views.ViewBookingModelData, name="view_booking_data"),

    path("Update_ProductCat/<int:id>/", views.UpdateProductCat, name="update_prod_cat"),
    path("Update_Product/<int:id>/", views.UpdateProductView, name="update_prod_view"),

    path("Delete_Product/<int:id>/", views.DeleteProductView, name="del_prod_view"),
    path("Delete_ProductCat/<int:id>/", views.DeleteProductCatView, name="del_prod_cat_view"),
    path("Delete_Booking/<int:id>/", views.DeleteBookingView, name="del_booking_view"),

]