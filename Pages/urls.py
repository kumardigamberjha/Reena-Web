from django.urls import path
from Pages import views

urlpatterns = [
    path('', views.EditPageView, name="editpage"),
    path('HomePage/', views.HomePageView, name="homepage"),
    path('AboutPage/', views.AboutusPageView, name="aboutpage"),
    path('DermaEdit/', views.DermaLogicaEditPage, name="dermaeditpage"),
    path('CaciEditPage/', views.CaciEditPage, name="cacieditpage"),
    path('IPLEdit/', views.iplEditPage, name="ipleditpage"),
    path('WaxEdit/', views.waxEditPage, name="waxeditpage"),
    path('NailEdit/', views.NailEditPage, name="naileditpage"),
    path('MakeEdit/', views.MakeUpEditPage, name="makeeditpage"),
    path('TintingEdit/', views.TintingEditPage, name="tineditpage"),
    path('EarEdit/', views.EarEditPage, name="eareditpage"),
    path('ElectroEdit/', views.ElecEditPage, name="electroeditpage"),
    path('ManEdit/', views.ManEditPage, name="maneditpage"),
    path('MassageEdit/', views.MassageEditPage, name="massageeditpage"),
    path('ContactUsView/', views.ContactUsEditPage, name="contacteditpage"),
    path('ContactEditUsView/<int:id>/', views.ShowContactPage, name="showcontact"),

]