from django.shortcuts import render, redirect
from website.models import ContactUsPage, Homepage, AboutUsPage
from website.forms import ContactForm, HomeForm, AboutUsForm
from Booking.forms import BookingModelForm, ProductCatForm, ProductForm
from Booking.models import BookingModel, ProductModel, ProductCat
from django.http import JsonResponse, HttpResponse
from django.contrib import messages


def Index(request):
    form = BookingModelForm()
    data = ProductModel.objects.all()
    homepage = Homepage.objects.all()[0]

    if request.method == "POST":
        form = BookingModelForm(request.POST)

        payment_status = request.POST.get('payment_status')
        datentime = request.POST.get('datentime')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        total_payment = request.POST.get('total_payment')

        if payment_status == "PaymentisDonecheckit":
            if BookingModel.objects.filter(datentime=datentime).exists():
                response = JsonResponse({"error": form.errors})
                response.status_code = 403
                return response
                
            elif form.is_valid():
                s = form.save()
                s.save()
                print(s.id)
                print("Form Saved")
                print("Form ID: ", s.pk)
                return redirect(f"Booking/View_BookingData/{s.id}")
            else:
                messages.success(request, form.errors)
                print("Form Error: ", form.errors)
                response = JsonResponse({"error":form.errors})
                response.status_code = 403
                return response
        else:
            print("Form Error", form.errors)
            messages.success(request, "Please Do Payment before Submittig")
            return HttpResponse("Please Check this error: ", form.errors)
    context = {'data': data, 'form': form, 'homepage':homepage}
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
    allprod = ProductModel.objects.all()
    allprodcat = ProductCat.objects.all()
    context = {'allprod': allprod, 'allprodcat': allprodcat}
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


def EditTextView(request):
    home = Homepage.objects.all()[0]
    homeform = HomeForm(instance=home)
    if request.method == "POST":
        homeform = HomeForm(request.POST, instance=home)
        if homeform.is_valid():
            homeform.save()
            print("Form Saved")
        else:
            print("Form Error: ", homeform.errors)

        
    # ########### About Us ################## 
    about = AboutUsPage.objects.all()[0]
    aboutform = AboutUsForm(instance=about)
    if request.method == "POST":
        aboutform = AboutUsForm(request.POST, instance=about)
        if aboutform.is_valid():
            aboutform.save()
            print("Form Saved")
        else:
            print("Form Error: ", aboutform.errors)

    allprodcat = ProductCat.objects.all()
    prodcat = ProductCatForm()
    if request.method == "POST":
        prodcat = ProductCatForm(request.POST)
        if prodcat.is_valid():
            prodcat.save()
            print("Form Saved")
        else:
            print("Form Error: ", prodcat.errors)

    allprod = ProductModel.objects.all()
    prodform = ProductForm()
    if request.method == "POST":
        prodcat = ProductForm(request.POST)
        if prodform.is_valid():
            prodform.save()
            print("Form Saved")
        else:
            print("Form Error: ", prodcat.errors)

    
    context = {'home': home, 'about': about, 'aboutform': aboutform, 'homeform':homeform, 'prodcat':prodcat, 'prodform': prodform, 'allprod':allprod, 'allprodcat': allprodcat}
    return render(request, 'website/Edit.html', context)
