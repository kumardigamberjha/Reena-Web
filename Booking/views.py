from django.shortcuts import render, redirect
from Booking.models import  ProductModel, ProductCat
from Booking.forms import ProductCatForm, ProductForm
from django.contrib import messages
from website.models import CartBookingModel, Timings
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
import datetime
import json
from website.forms import CartBookingForm
from django.contrib.auth.models import User


@login_required
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


@login_required
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
    messages.success(request, 'Category Deleted Successfully')
    
    return redirect('show_product_cat_model')



##################### Product Model #######################
@login_required
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


@login_required
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
    messages.success(request, 'Form Saved')
    
    return redirect('show_product_model')


@login_required
def AddBookingView(request):
    # form = CartBookingModelForm()
    # data = ProductModel.objects.all()
    # if request.method == "POST":
    #     form = CartBookingModelForm(request.POST)

    #     payment_status = request.POST.get('payment_status')
    #     datentime = request.POST.get('datentime')
    #     name = request.POST.get('name')
    #     phone = request.POST.get('phone')
    #     total_payment = request.POST.get('total_payment')

    #     if payment_status == "PaymentisDonecheckit":
    #         if CartBookingModel.objects.filter(datentime=datentime).exists():
    #             response = JsonResponse({"error": form.errors})
    #             response.status_code = 403 # To announce that the user isn't allowed to publish
    #             return response
                
    #         elif form.is_valid():
    #             form.save()
    #             print("Form Saved")
    #             print("Form Values: ", form)
    #             print("Request POST: ", request.POST)

    #             return redirect("add_product_view")
    #         else:
    #             messages.success(request, form.errors)
    #             print("Form Error: ", form.errors)
    #             response = JsonResponse({"error":form.errors})
    #             response.status_code = 403
    #             return response
    #     else:
    #         print("Form Error", form.errors)
    #         messages.success(request, "Please Do Payment before Submittig")
            # return HttpResponse("Please Check this error: ", form.errors)


    # context = {'form': form, 'data': data}
    return render(request, 'Booking/add_booking.html')


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



# Booking Date and Time From Jquery
def GetBookingDatentime(request):
    if request.method == "POST":
        date = request.POST.get("date")
        # time = request.POST.get("time")
    
        print("Date: ", date)
        # print("Time: ", time)
        times = CartBookingModel.objects.filter(date=date)
        bookingTime = []
        for i in times:
            # print(i.name)
            # print(i.date)
            # print(i.time)
            bookingTime.append(i.time)
        print("Booking Time: ", bookingTime)
        alltimings = Timings.objects.all()
        allslots = []
        for i in alltimings:
            allslots.append(i)

        result = [value for value in allslots if value not in bookingTime]
        print("Result: ", result)
        if result == []:
            result = allslots
            print("Empty: ", result)

        bookingTimes = serializers.serialize('json', result)
        print("bookingTimes: ", bookingTimes)
        if CartBookingModel.objects.filter(date=date).exists():
            amount = "Time Slot is already Taken"
            print(amount)
            return JsonResponse({'amount' : amount, 'times': bookingTimes}, status=200)

        else:
            amount = "Ready To Go"
            print(amount)
            return JsonResponse({'amount' : amount, 'times': bookingTimes}, status=200)
    else:
        amount = "Ready To Go"
        return JsonResponse({'amount' : amount}, status=200)


@login_required
def ShowBookingModel(request):
    if request.user.is_superuser:
        data = CartBookingModel.objects.all().order_by('-BookingTime')
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


@login_required
def ViewBookingModelData(request, id):
    data = CartBookingModel.objects.get(id=id)
    total = 0
    arr = []
    services = []
    somedata = json.loads(data.services)
    
    print("somedata: ", somedata)

    context = {'data': data, 'total': total, 'somedata': somedata, 'services': services}
    return render(request, "Booking/viewBooking.html", context)

import ast
@login_required
def UpdateBookingModelData(request, id):
    # somedata = []    
    
    data = CartBookingModel.objects.get(id=id)
    somedata = json.loads(data.services)
    form = CartBookingForm(instance=data)
    if request.method == "POST":
        date = request.POST.get('date')
        print("Date: ", date)
        form = CartBookingForm(request.POST, instance=data)
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
        print("Se: ", se)
    
        print("somedata: ", somedata)

        if form.is_valid():
            form.save()
            print("Form Saved")
            messages.success(request, 'Updated')
            return redirect('show_booking')
            
        else:
            print("Form Error")
            messages.success(request, f'Form Error: {form.errors}' )
            
        # booking = CartBookingModel(name=name,phone=phone, email=email, date=date, time=time, total_payment=total_payment, services=services, foruser=foruser)
        # booking.save()
        # print("Value Saved")

    total = 0
    arr = []
    services = []    

    context = {'data': data, 'total': total, 'services': services, 'form': form, 'somedata': somedata}
    return render(request, "Booking/updateBooking.html", context)

@login_required
def Accounts(request):
    data = CartBookingModel.objects.all().order_by('-date')
    total = 0
    for i in data:
        total += int(i.total_payment)
    context = {'data': data, 'total': total}
    return render(request, 'Booking/accounts.html', context)


@login_required
def DeleteBookingView(request, id):
    CartBookingModel.objects.filter(id=id).delete()
    messages.success(request, 'Deleted')
    return redirect('show_booking')


# @login_required
# def TodayBooking(request):
#     somemonth = datetime.date.today()
#     somemonth_str = somemonth.strftime('%Y-%m-%d')
#     months = somemonth.month
#     data = CartBookingModel.objects.filter(appointmentdate__date = somemonth)
#     context = {'data': data, 'somemonth': somemonth}
#     return render(request, 'Booking/today_book.html', context)


@login_required
def TodayAppointment(request):
    somemonth = datetime.date.today()
    months = somemonth.month
    data = CartBookingModel.objects.filter(BookingTime__date = somemonth)
    context = {'data': data, 'somemonth': somemonth}
    return render(request, 'Booking/today_appointment.html', context)