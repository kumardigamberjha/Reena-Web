from django.shortcuts import render, redirect
from Booking.models import BookingModel, ProductModel, ProductCat
from Booking.forms import ProductCatForm, ProductForm, BookingModelForm
from django.contrib import messages
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
import datetime

def AddProductCat(request):
    form = ProductCatForm()

    if request.method == "POST":
        form = ProductCatForm(request.POST)

        if form.is_valid():
            form.save()
            print("Form Saved")
            messages.success(request, 'Form Saved')
        else:
            messages.success(request, 'Form Error: ', form.errors)
        
    context = {'form': form}
    return render(request, 'Booking/add_product_cat.html', context)


def UpdateProductCat(request, id):
    prodcatid = ProductCat.objects.get(id=id)
    form = ProductCatForm(instance=prodcatid)

    if request.method == "POST":
        form = ProductCatForm(request.POST, instance=prodcatid)

        if form.is_valid():
            form.save()
            print("Form Saved")
            messages.success(request, 'Form Saved')
        else:
            messages.success(request, 'Form Error: ', form.errors)
        
    context = {'form': form, 'prodcatid':prodcatid}
    return render(request, 'Booking/add_product_cat.html', context)


@login_required
def DeleteProductCatView(request, id):
    ProductCat.objects.filter(id=id).delete()
    return redirect('show_product_cat_model')



##################### Product Model #######################
def AddProductView(request):
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            print("Form Saved")
            messages.success(request, 'Form Saved')

        else:
            messages.success(request, 'Form Error: ', form.errors)
        
    context = {'form': form}
    return render(request, 'Booking/add_product.html', context)


def UpdateProductView(request, id):
    prodid = ProductModel.objects.get(id = id)
    form = ProductForm(instance=prodid)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=prodid)

        if form.is_valid():
            form.save()
            print("Form Saved")
            messages.success(request, 'Form Saved')

        else:
            messages.success(request, 'Form Error: ', form.errors)
        
    context = {'form': form, 'prodid':prodid}
    return render(request, 'Booking/add_product.html', context)


@login_required
def DeleteProductView(request, id):
    ProductModel.objects.filter(id=id).delete()
    return redirect('show_product_model')

def AddBookingView(request):
    form = BookingModelForm()
    data = ProductModel.objects.all()
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
                response.status_code = 403 # To announce that the user isn't allowed to publish
                return response
                
            elif form.is_valid():
                form.save()
                print("Form Saved")
                print("Form Values: ", form)
                print("Request POST: ", request.POST)

                return redirect("add_product_view")
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


    context = {'form': form, 'data': data}
    return render(request, 'Booking/add_booking.html', context)


def GetBookingPrice(request):
    if request.method == "GET":
        services = request.GET.getlist("services[]")
        print("Services: ", services)
    amount = 0
    arr = []
    for i in services:
        clientdata = ProductModel.objects.filter(id=i)
        arr.append(clientdata)
        
    print("Services: ", services)
    
    print("Arr: ", arr)
    for i in arr:
        for j in i:
            amount += j.price
    
    print("Amount: ", amount)

    return JsonResponse({'amount' : amount}, status=200)




def GetBookingDatentime(request):
    if request.method == "POST":
        datentime = request.POST.get("datentime")

    if BookingModel.objects.filter(datentime=datentime).exists():
        amount = "Time Slot is already Taken"
        return JsonResponse({'amount' : amount}, status=200)

    else:
        amount = "Ready To Go"
        return JsonResponse({'amount' : amount}, status=200)


@login_required
def ShowBookingModel(request):
    if request.user.is_superuser:
        data = BookingModel.objects.all()
        context = {'data': data}
        return render(request, "Booking/show_booking.html", context)
    context = {}
    return render(request, "Booking/show_booking.html", context)


@login_required
def ShowProductModel(request):
    if request.user.is_superuser:
        data = ProductModel.objects.all()
        context = {'data': data}
        return render(request, "Booking/Show_Product.html", context)
    context = {}
    return render(request, "Booking/Show_Product.html", context)


@login_required
def ShowProductCategoryModel(request):
    if request.user.is_superuser:
        data = ProductCat.objects.all()
        context = {'data': data}
        return render(request, "Booking/show_prod_cat.html", context)
    context = {}
    return render(request, "Booking/show_prod_cat.html", context)


def ViewBookingModelData(request, id):
    data = BookingModel.objects.get(id=id)
    total = 0
    for i in data.services.all():
        total += i.price
    context = {'data': data, 'total': total}
    return render(request, "Booking/viewBooking.html", context)


@login_required
def Accounts(request):
    data = BookingModel.objects.all()
    total = 0
    for i in data:
        total += int(i.total_payment)
    context = {'data': data, 'total': total}
    return render(request, 'Booking/accounts.html', context)


@login_required
def DeleteBookingView(request, id):
    BookingModel.objects.filter(id=id).delete()
    return redirect('show_booking')


@login_required
def TodayBooking(request):
    somemonth = datetime.date.today()
    months = somemonth.month
    data = BookingModel.objects.filter(datentime__date = somemonth)
    context = {'data': data, 'somemonth': somemonth}
    return render(request, 'Booking/today_book.html', context)


@login_required
def TodayAppointment(request):
    somemonth = datetime.date.today()
    months = somemonth.month
    data = BookingModel.objects.filter(BookingTime__date = somemonth)
    context = {'data': data, 'somemonth': somemonth}
    return render(request, 'Booking/today_book.html', context)