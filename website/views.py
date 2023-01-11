from django.shortcuts import render, redirect
from website.models import ContactUsPage
from website.forms import ContactForm


def Index(request):
    context = {}
    return render(request, 'website/index.html', context)


def AboutUs(request):
    context = {}
    return render(request, 'website/aboutus.html', context)


def Services(request):
    context = {}
    return render(request, 'website/Services.html', context)


def RewardsView(request):
    context = {}
    return render(request, 'website/gifts.html', context)


def Pricing(request):
    context = {}
    return render(request, 'website/pricing.html', context)


def Pricing(request):
    context = {}
    return render(request, 'website/pricing.html', context)


def DermalogicaView(request):
    context = {}
    return render(request, 'website/dermalogica.html', context)
    

def CACIView(request):
    context = {}
    return render(request, 'website/CaciSynergy.html', context)


def Contact(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            print("Form Saved")
            return redirect("/")
    context = {'form': form}
    return render(request, 'website/contactus.html', context)


def IPLView(request):
    context = {}
    return render(request, 'website/Elight.html', context)


def WaxingView(request):
    context = {}
    return render(request, 'website/waxing.html', context)


def EarpView(request):
    context = {}
    return render(request, 'website/Ear Piercing.html', context)


def TintingView(request):
    context = {}
    return render(request, 'website/Tinting.html', context)


def ElectroView(request):
    context = {}
    return render(request, 'website/Electrolysis.html', context)


def ManicureandPedicure(request):
    context = {}
    return render(request, 'website/manicurepedicure.html', context)


def MassageView(request):
    context = {}
    return render(request, 'website/Massage.html', context)


def BridalServicesView(request):
    context = {}
    return render(request, 'website/BridalServices.html', context)


def HennaView(request):
    context = {}
    return render(request, 'website/Henna.html', context)


def NailExtensionView(request):
    context = {}
    return render(request, 'website/Nailextension.html', context)
