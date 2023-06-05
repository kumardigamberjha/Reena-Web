from django.urls import path
from website import views

urlpatterns = [
    path('', views.Index, name="index"),
    path('aboutus/', views.AboutUs, name="aboutus"),
    path('Services/', views.Services, name="services"),
    path('Pricing/', views.Pricing, name="pricing"),
    
    path('Pricing/<str:category>/', views.Pricing, name="pricingCat"),
    path('contact/', views.Contact, name="contactus"),
    path('dermalogica/', views.DermalogicaView, name="dermalogica"),
    path('CACISynergy/', views.CACIView, name="caciview"),
    path('elight/', views.IPLView, name="iplview"),
    path('waxing/', views.WaxingView, name="waxingview"),
    path('EarPiercing/', views.EarpView, name="earpview"),
    path('Electrolysis/', views.ElectroView, name="electroview"),
    path('manicureandpedicure/', views.ManicureandPedicure, name="manicureview"),
    path('Massage/', views.MassageView, name="massageview"),
    path('Tinting/', views.TintingView, name="tintingview"),
    path('NailExtension/', views.NailExtensionView, name="nailextview"),
    path('BridalMakeUp/', views.BridalServicesView, name="bridalview"),
    path('NailExtension/', views.NailExtensionView, name="nailextview"),
    path('Henna/', views.HennaView, name="Hennaview"),
    path('Rewards/', views.RewardsView, name="rewards"),
    # path('Checkoutpage/', views., name="cart"),

    path('Cart/', views.CartAndBooking, name="cart"),
    path('DelAllBookingCartItems/', views.DelAllBooking, name="delallbookingcart"),
    path('DelBookingCartItem/<int:id>/', views.DelCartBooking, name="delbookingcart"),

    path('Documents/', views.DocumentsPage, name="documents"),
    path('ForgetPassword/', views.ForgetPassword, name="forgetpassword"),

    path('ShowUsersBooking/', views.ShowUsersBookings, name="user_bookings"),

]