from django.shortcuts import render, redirect
from website.models import ContactUsPage, CartItem, CartBookingModel, Timings
from website.forms import ContactForm, HomeForm, AboutUsForm, CartForm, CartBookingForm
from Pages.models import Homepage, AboutUsPage, DermaLogicaPage, CaciSynergyPage, IPLPage, WaxingPage, NailPage, MakeUpPage, TintingPage, EarPage, ElectroPage, ManPage, MassagePage, GiftPage, AddItemModel,NewPage, PayPalIntegration
from Booking.forms import BookingModelForm, ProductCatForm, ProductForm
from Booking.models import BookingModel, ProductModel, ProductCat
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core.mail import send_mail
from Reena.settings import EMAIL_HOST_USER
import random

def Index(request):
    prods = ProductModel.objects.all()
    homepage = Homepage.objects.all()[0]
    cats = ProductCat.objects.all()
    new_page = NewPage.objects.all()

    form = BookingModelForm()
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
            
    context = { 'new_page': new_page, 'prods': prods, 'form': form, 'homepage':homepage, 'cat': cats, 'new_page': new_page}
    return render(request, 'website/index.html', context)


def AboutUs(request):
    about = AboutUsPage.objects.all()[0]
    cats = ProductCat.objects.all()
    prods = ProductModel.objects.all()
    new_page = NewPage.objects.all()
    form = BookingModelForm()
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

    context = {'prods':prods, 'form': form, 'about': about, 'cat': cats, 'new_page': new_page}
    return render(request, 'website/aboutus.html', context)


def Services(request):
    cats = ProductCat.objects.all()
    prods = ProductModel.objects.all()
    new_page = NewPage.objects.all()
    form = BookingModelForm()
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
    context = { 'new_page': new_page, 'prods':prods, 'form': form, 'cat':cats}
    return render(request, 'website/Services.html', context)


def RewardsView(request):
    gift = GiftPage.objects.all()[0]
    cats = ProductCat.objects.all()
    prods = ProductModel.objects.all()
    new_page = NewPage.objects.all()
    form = BookingModelForm()
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
    context = { 'new_page': new_page, 'prods':prods, 'form': form, 'gift': gift, 'cat':cats}
    return render(request, 'website/gifts.html', context)

@csrf_exempt
def Pricing(request, category=None):
    new_page = NewPage.objects.all()
    if category:
        # Logic for the pricing page with a specific category
        print("Category")
    else:
        # Logic for the pricing page without a specific category
        print("None")

    allprodcat = ProductCat.objects.all()
    cats = ProductCat.objects.all()
    prods = ProductModel.objects.all()

    cartitems = None
    if request.user.is_authenticated:
        cartitems = CartItem.objects.filter(foruser=request.user)

    prods = ProductModel.objects.all()

    cartitem_names = [item.name for item in cartitems] if cartitems else []

    form = CartForm()
    if request.method == "POST":
        name = request.POST.get('name')
        foruser = request.POST.get('foruser')

        form = CartForm(request.POST)
        print("Name: ", name)
        if not CartItem.objects.filter(name=name, foruser=foruser).exists():
            if form.is_valid():
                s = form.save()
                s.save()
                messages.success(request, "Item Added To Cart")
                print("Form Saved")
            else:
                messages.success(request, "Some Error")
                print("Form Error: ", form.errors)
        else:
            messages.success(request, "Item already Exists in Cart")
            print("Item Already Exists")

    context = { 'new_page': new_page, 'prods': prods, 'form': form, 'cat': cats, 'allprodcat': allprodcat, 'cartitem_names': cartitem_names}
    return render(request, 'website/pricing.html', context)


# def Pricing(request, category=None):
#     if category:
#         # Logic for the pricing page with a specific category
#         pass
#         print("Category")
#     else:
#         # Logic for the pricing page without a specific category
#         # pass
#         print("None")
#     allprodcat = ProductCat.objects.all()
#     cats = ProductCat.objects.all()
#     prods = ProductModel.objects.all()
#     try:
#         cartitems = CartItem.objects.filter(foruser=request.user)
#     except:
#         cartitems = None
#     # for i in prods:
#     #     for j in cartitems:
#     #         print(f"{i.name} and {j.name}" ,i.name == j.name)

#     prods = ProductModel.objects.all()
    
#     # cartitems = CartItem.objects.filter(foruser=request.user)

#     cartitem_names = set([j.name for j in cartitems])
    
#     form = CartForm()
#     if request.method == "POST":
#         name = request.POST.get('name')
#         foruser = request.POST.get('foruser')

#         form = CartForm(request.POST)
#         print("Name: ", name)
#         if not CartItem.objects.filter(name=name, foruser=foruser).exists():
#             if form.is_valid():
#                 s = form.save()
#                 s.save()
#                 messages.success(request, "Item Added To Cart")
#                 print("Form Saved")
#             else:
#                 messages.success(request, "Some Error")
#                 print("Form Error: ", form.errors)
#         else:
#             messages.success(request, "Item already Exists in Cart")
#             print("Item Already Existes")

#     cartitem_names = [item.name for item in cartitems]
    
#     context = { 'new_page': new_page, 'prods':prods, 'form':form, 'cat':cats, 'allprodcat': allprodcat,  'cartitem_names': cartitem_names}
#     return render(request, 'website/pricing.html', context)


def DermalogicaView(request):
    derma = DermaLogicaPage.objects.all()[0]
    cats = ProductCat.objects.all()
    prods = ProductModel.objects.all()
    new_page = NewPage.objects.all()
    form = BookingModelForm()
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
    context = { 'new_page': new_page, 'prods':prods, 'form': form, 'derma': derma,'cat': cats}
    return render(request, 'website/dermalogica.html', context)
    

def CACIView(request):
    caci = CaciSynergyPage.objects.all()[0]
    new_page = NewPage.objects.all()
    cats = ProductCat.objects.all()
    prods = ProductModel.objects.all()
    form = BookingModelForm()
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
    context = { 'new_page': new_page, 'prods':prods, 'form': form, 'caci': caci, 'cat':cats}
    return render(request, 'website/CaciSynergy.html', context)


def Contact(request):
    form = ContactForm()
    new_page = NewPage.objects.all()

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            print("Form Saved")
            return redirect("/")
        else:
            print("Form Error: ", form.errors)
    context = { 'new_page': new_page, 'form': form}
    return render(request, 'website/contactus.html', context)


def IPLView(request):
    ipl = IPLPage.objects.all()[0]
    cats = ProductCat.objects.all()
    new_page = NewPage.objects.all()
    prods = ProductModel.objects.all()
    form = BookingModelForm()
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
    context = { 'new_page': new_page, 'prods':prods, 'form': form, 'ipl': ipl, 'cat': cats}
    return render(request, 'website/Elight.html', context)


def WaxingView(request):
    wax = WaxingPage.objects.all()[0]
    new_page = NewPage.objects.all()
    cats = ProductCat.objects.all()
    prods = ProductModel.objects.all()
    form = BookingModelForm()
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
    context = { 'new_page': new_page, 'prods':prods, 'form': form, 'wax': wax, 'cat': cats}
    return render(request, 'website/waxing.html', context)


def EarpView(request):
    new_page = NewPage.objects.all()
    ear = EarPage.objects.all()[0]
    cats = ProductCat.objects.all()
    prods = ProductModel.objects.all()
    form = BookingModelForm()
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
    context = { 'new_page': new_page, 'prods':prods, 'form': form, 'ear': ear, 'cat': cats}
    return render(request, 'website/Ear Piercing.html', context)


def TintingView(request):
    tin = TintingPage.objects.all()[0]
    new_page = NewPage.objects.all()
    cats = ProductCat.objects.all()
    prods = ProductModel.objects.all()
    form = BookingModelForm()
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
            
    context = { 'new_page': new_page, 'prods':prods,'form': form, 'tin': tin, 'cat': cats}
    return render(request, 'website/Tinting.html', context)


def ElectroView(request):
    electro = ElectroPage.objects.all()[0]
    new_page = NewPage.objects.all()
    cats = ProductCat.objects.all()
    prods = ProductModel.objects.all()
    form = BookingModelForm()
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
    context = { 'new_page': new_page, 'prods':prods, 'form': form, 'electro': electro, 'cat': cats}
    return render(request, 'website/Electrolysis.html', context)


def ManicureandPedicure(request):
    man = ManPage.objects.all()[0]
    new_page = NewPage.objects.all()
    cats = ProductCat.objects.all()
    prods = ProductModel.objects.all()
    form = BookingModelForm()
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
    context = { 'new_page': new_page, 'prods':prods, 'form': form, 'man': man, 'cat': cats}
    return render(request, 'website/manicurepedicure.html', context)


def MassageView(request):
    massage = MassagePage.objects.all()[0]
    new_page = NewPage.objects.all()
    cats = ProductCat.objects.all()
    prods = ProductModel.objects.all()
    form = BookingModelForm()
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

    context = { 'new_page': new_page, 'prods':prods, 'form': form, 'massage': massage, 'cat': cats}
    return render(request, 'website/Massage.html', context)


def BridalServicesView(request):
    makeup = MakeUpPage.objects.all()[0]
    new_page = NewPage.objects.all()
    cats = ProductCat.objects.all()
    prods = ProductModel.objects.all()
    form = BookingModelForm()
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
    context = { 'new_page': new_page, 'prods':prods, 'form': form, 'makeup': makeup, 'cat': cats}
    return render(request, 'website/BridalServices.html', context)


def HennaView(request):
    cats = ProductCat.objects.all()
    prods = ProductModel.objects.all()
    new_page = NewPage.objects.all()
    form = BookingModelForm()
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
    context = { 'new_page': new_page, 'prods':prods, 'form': form, 'cat': cats}
    return render(request, 'website/Henna.html', context)


def NailExtensionView(request):
    nail = NailPage.objects.all()[0]
    new_page = NewPage.objects.all()
    cats = ProductCat.objects.all()
    prods = ProductModel.objects.all()
    form = BookingModelForm()
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
    context = { 'new_page': new_page, 'prods':prods, 'form': form, 'nail': nail, 'cat':cats}
    return render(request, 'website/Nailextension.html', context)


@login_required
def CartAndBooking(request):
    allitems = CartItem.objects.filter(foruser=request.user)
    new_page = NewPage.objects.all()
    form = CartBookingForm()
    lenofcart = len(allitems)
    paypal = PayPalIntegration.objects.get(id=1)
    s = 0
    items = CartItem.objects.filter(foruser = request.user.id)
    for i in items:
        s += i.price

    if request.method == "POST":
        form = CartBookingForm(request.POST)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        someuser = request.POST.get('foruser')
        foruser = User.objects.get(id=someuser)
        date = request.POST.get('date')
        stime = request.POST.get('time')
        time = Timings.objects.get(id=stime)
        se = request.POST.getlist('services')
        total_payment = request.POST.get('total_payment')
        services = json.dumps(se)
        print("Services: ", services)
        booking = CartBookingModel(name=name,phone=phone, email=email, date=date, time=time, total_payment=total_payment, services=services, foruser=foruser)
        booking.save()
        print("Value Saved")

    context={'new_page': new_page, 'allitems':allitems, 'total': s, 'length':lenofcart, 'paypal': paypal}
    return render(request, 'website/checkoutpage.html', context)


def DocumentsPage(request):
    new_page = NewPage.objects.all()
    context = {'new_page': new_page}
    return render(request, 'website/Documents.html', context)


def DelCartBooking(request, id):
    item = CartItem.objects.get(id=id)
    item.delete()
    print("Item Deleted")
    return redirect('cart')


def DelAllBooking(request):
    if request.method == "POST":
        foruser = request.POST.get('foruser')
        
        item = CartItem.objects.filter(foruser=foruser)
        print("Item: ", item)
        for i in item:
            i.delete()
        print("All Item Deleted")
    return redirect('cart')


@login_required
def ShowUsersBookings(request):
    new_page = NewPage.objects.all()
    usersBooking = CartBookingModel.objects.filter(foruser=request.user.id)
    arr = []    
    for i in usersBooking:
        arr.append(i)
    print("Arr: ", arr)

    context = { 'new_page': new_page, 'userBookings': usersBooking, 'arr': arr}
    return render(request, 'Booking/show_users_booking.html', context)



def ForgetPassword(request):
    if request.method == "POST":
        email = request.POST.get('email')
        print("Email: ", email)

    # otp = random.randint(111111, 999999)
    # print("OTP: ", otp)
    context = { }
    return render(request, 'website/forgetPassword.html', context)