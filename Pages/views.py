from django.shortcuts import render
from Pages.models import DermaLogicaPage, Homepage, AboutUsPage, IPLPage, EarPage, ElectroPage, MakeUpPage, ManPage, MassagePage, CaciSynergyPage, GiftPage, NailPage, WaxingPage, TintingPage
from website.forms import DermaForm, HomeForm, AboutUsForm

def EditPageView(request):
    context = {}
    return render(request, 'Pages/editpage.html', context)


def HomePageView(request):
    home = Homepage.objects.all()[0]
    homeform = HomeForm(instance=home)
    if request.method == "POST":
        homeform = HomeForm(request.POST, instance=home)
        if homeform.is_valid():
            homeform.save()
            print("Form Saved")
        else:
            print("Form Error: ", homeform.errors)
    context = {'home': home, 'homeform': homeform}
    return render(request, 'Pages/homepage.html', context)


def AboutusPageView(request):
    about = AboutUsPage.objects.all()[0]
    aboutform = AboutUsForm(instance=about)
    if request.method == "POST":
        aboutform = AboutUsForm(request.POST, instance=about)
        if aboutform.is_valid():
            aboutform.save()
            print("Form Saved")
        else:
            print("Form Error: ", aboutform.errors)
    context = {'about': about, 'aboutform': aboutform}
    return render(request, 'Pages/aboutusedit.html', context)