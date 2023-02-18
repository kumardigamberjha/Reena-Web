from django.shortcuts import render, redirect
from website.models import ContactUsPage, CartItem, CartBookingModel
from website.forms import ContactForm, HomeForm, AboutUsForm, CartForm, CartBookingForm
from Pages.models import Homepage, AboutUsPage, DermaLogicaPage, CaciSynergyPage, IPLPage, WaxingPage, NailPage, MakeUpPage, TintingPage, EarPage, ElectroPage, ManPage, MassagePage, GiftPage
from Booking.forms import BookingModelForm, ProductCatForm, ProductForm
from Booking.models import BookingModel, ProductModel, ProductCat
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


def Index(request):
    prods = ProductModel.objects.all()
    homepage = Homepage.objects.all()[0]
    cats = ProductCat.objects.all()
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
            
    context = {'prods': prods, 'form': form, 'homepage':homepage, 'cat': cats}
    return render(request, 'website/index.html', context)


def AboutUs(request):
    about = AboutUsPage.objects.all()[0]
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

    context = {'prods':prods, 'form': form, 'about': about, 'cat': cats}
    return render(request, 'website/aboutus.html', context)


def Services(request):
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
    context = {'prods':prods, 'form': form, 'cat':cats}
    return render(request, 'website/Services.html', context)


def RewardsView(request):
    gift = GiftPage.objects.all()[0]
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
    context = {'prods':prods, 'form': form, 'gift': gift, 'cat':cats}
    return render(request, 'website/gifts.html', context)


@csrf_exempt
def Pricing(request):
    allprodcat = ProductCat.objects.all()
    cats = ProductCat.objects.all()
    prods = ProductModel.objects.all()
    form = CartForm()
    if request.method == "POST":
        name = request.POST.get('name')
        form = CartForm(request.POST)
        print("Name: ", name)
        if not CartItem.objects.filter(name=name).exists():
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
            print("Item Already Existes")

    context = {'prods':prods, 'form':form, 'cat':cats, 'allprodcat': allprodcat, }
    return render(request, 'website/pricing.html', context)


def DermalogicaView(request):
    derma = DermaLogicaPage.objects.all()[0]
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
    context = {'prods':prods, 'form': form, 'derma': derma,'cat': cats}
    return render(request, 'website/dermalogica.html', context)
    

def CACIView(request):
    caci = CaciSynergyPage.objects.all()[0]
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
    context = {'prods':prods, 'form': form, 'caci': caci, 'cat':cats}
    return render(request, 'website/CaciSynergy.html', context)


def Contact(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            print("Form Saved")
            return redirect("/")
        else:
            print("Form Error: ", form.errors)
    context = {'form': form}
    return render(request, 'website/contactus.html', context)


def IPLView(request):
    ipl = IPLPage.objects.all()[0]
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
    context = {'prods':prods, 'form': form, 'ipl': ipl, 'cat': cats}
    return render(request, 'website/Elight.html', context)


def WaxingView(request):
    wax = WaxingPage.objects.all()[0]
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
    context = {'prods':prods, 'form': form, 'wax': wax, 'cat': cats}
    return render(request, 'website/waxing.html', context)


def EarpView(request):
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
    context = {'prods':prods, 'form': form, 'ear': ear, 'cat': cats}
    return render(request, 'website/Ear Piercing.html', context)


def TintingView(request):
    tin = TintingPage.objects.all()[0]
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
            
    context = {'prods':prods,'form': form, 'tin': tin, 'cat': cats}
    return render(request, 'website/Tinting.html', context)


def ElectroView(request):
    electro = ElectroPage.objects.all()[0]
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
    context = {'prods':prods, 'form': form, 'electro': electro, 'cat': cats}
    return render(request, 'website/Electrolysis.html', context)


def ManicureandPedicure(request):
    man = ManPage.objects.all()[0]
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
    context = {'prods':prods, 'form': form, 'man': man, 'cat': cats}
    return render(request, 'website/manicurepedicure.html', context)


def MassageView(request):
    massage = MassagePage.objects.all()[0]
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

    context = {'prods':prods, 'form': form, 'massage': massage, 'cat': cats}
    return render(request, 'website/Massage.html', context)


def BridalServicesView(request):
    makeup = MakeUpPage.objects.all()[0]
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
    context = {'prods':prods, 'form': form, 'makeup': makeup, 'cat': cats}
    return render(request, 'website/BridalServices.html', context)


def HennaView(request):
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
    context = {'prods':prods, 'form': form, 'cat': cats}
    return render(request, 'website/Henna.html', context)


def NailExtensionView(request):
    nail = NailPage.objects.all()[0]
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
    context = {'prods':prods, 'form': form, 'nail': nail, 'cat':cats}
    return render(request, 'website/Nailextension.html', context)


def CartAndBooking(request):
    allitems = CartItem.objects.all()
    form = CartBookingForm()
    lenofcart = len(allitems)
    s = 0
    for i in allitems:
        s += i.price
    if request.method == "POST":
        form = CartBookingForm(request.POST)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        services = request.POST.getlist('services')
        total_payment = request.POST.get('total_payment')
        print('name: ', name)
        print('phone: ', phone)
        print('email: ', email)
        print('services: ', services)
        print('total_payment: ', total_payment)
        if form.is_valid():
            form.save()
            print("Form Saved")
        else:
            print("Not Saved: ", form.errors)

    context={'allitems':allitems, 'total': s, 'length':lenofcart}
    return render(request, 'website/checkoutpage.html', context)


def DocumentsPage(request):
    return render(request, 'website/Documents.html')

def DelBooking(request, id):
    item = CartItem.objects.get(id=id)
    item.delete()
    return redirect('cart')