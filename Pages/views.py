from django.shortcuts import render
from Pages.models import DermaLogicaPage, Homepage, AboutUsPage, IPLPage, EarPage, ElectroPage, MakeUpPage, ManPage, MassagePage, CaciSynergyPage, GiftPage, NailPage, WaxingPage, TintingPage
from website.forms import DermaForm, HomeForm, AboutUsForm, CaciForm, IPLForm, WaxingForm, NailForm, MakeUpForm, TintingForm, EarPForm, ElectroForm, ManForm, MassageForm, ContactForm
from django.contrib.auth.decorators import login_required
from Booking.models import BookingModel
import datetime
from website.models import ContactUsPage

@login_required
def EditPageView(request):
    somemonth = datetime.date.today()
    months = somemonth.month
    todays_bookings_q = BookingModel.objects.filter(datentime__date=somemonth)
    todays_bookings = todays_bookings_q.count()
    todays_appointment_q = BookingModel.objects.filter(BookingTime__date=somemonth)
    todays_appointment = todays_appointment_q.count()
    monthly_appointment = BookingModel.objects.filter(BookingTime__month=months)
    mac = monthly_appointment.count()
    tb6 = todays_bookings_q[:5]
    ta6 = todays_appointment_q[:5]
    total = 0
    for i in monthly_appointment:
        total += int(i.total_payment)

    context = {'todays_bookings': todays_bookings, 'todays_appointment': todays_appointment, 'monthly_appointment': monthly_appointment, 'mac': mac, 'total': total, 'todays_bookings_q':todays_bookings_q, 'todays_appointment_q':todays_appointment_q, 'ta6': ta6, 'tb6': tb6}
    return render(request, 'Pages/editpage.html', context)

@login_required
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


@login_required
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


############## DERMALOGICA #################
@login_required
def DermaLogicaEditPage(request):
    derma = DermaLogicaPage.objects.all()[0]
    dermaform = DermaForm(instance=derma)
    if request.method == "POST":
        dermaform = DermaForm(request.POST, instance=derma)
        if dermaform.is_valid():
            dermaform.save()
            print("Form Saved")
        else:
            print("Form Error: ", dermaform.errors)
    context = {'derma': derma, 'dermaform': dermaform}
    return render(request, 'Pages/dermalogica.html', context)


############## CACI #################
@login_required
def CaciEditPage(request):
    caci = CaciSynergyPage.objects.all()[0]
    caciform = CaciForm(instance=caci)
    if request.method == "POST":
        caciform = CaciForm(request.POST, instance=caci)
        if caciform.is_valid():
            caciform.save()
            print("Form Saved")
        else:
            print("Form Error: ", caciform.errors)
    context = {'caci': caci, 'caciform': caciform}
    return render(request, 'Pages/caciedit.html', context)


############## IPL #################
@login_required
def iplEditPage(request):
    ipl = IPLPage.objects.all()[0]
    iplform = IPLForm(instance=ipl)
    if request.method == "POST":
        iplform = IPLForm(request.POST, instance=ipl)
        if iplform.is_valid():
            iplform.save()
            print("Form Saved")
        else:
            print("Form Error: ", iplform.errors)
    context = {'ipl': ipl, 'iplform': iplform}
    return render(request, 'Pages/ipledit.html', context)


@login_required
def waxEditPage(request):
    wax = WaxingPage.objects.all()[0]
    waxform = WaxingForm(instance=wax)
    if request.method == "POST":
        waxform = WaxingForm(request.POST, instance=wax)
        if waxform.is_valid():
            waxform.save()
            print("Form Saved")
        else:
            print("Form Error: ", waxform.errors)
    context = {'wax': wax, 'waxform': waxform}
    return render(request, 'Pages/waxedit.html', context)


@login_required
def NailEditPage(request):
    nail = NailPage.objects.all()[0]
    nailform = NailForm(instance=nail)
    if request.method == "POST":
        nailform = NailForm(request.POST, instance=nail)
        if nailform.is_valid():
            nailform.save()
            print("Form Saved")
        else:
            print("Form Error: ", nailform.errors)
    context = {'nail': nail, 'nailform': nailform}
    return render(request, 'Pages/nailedit.html', context)


@login_required
def MakeUpEditPage(request):
    make = MakeUpPage.objects.all()[0]
    makeform = MakeUpForm(instance=make)
    if request.method == "POST":
        makeform = MakeUpForm(request.POST, instance=make)
        if makeform.is_valid():
            makeform.save()
            print("Form Saved")
        else:
            print("Form Error: ", makeform.errors)
    context = {'make': make, 'makeform': makeform}
    return render(request, 'Pages/makeupedit.html', context)


@login_required
def TintingEditPage(request):
    tin = TintingPage.objects.all()[0]
    tinform = TintingForm(instance=tin)
    if request.method == "POST":
        tinform = TintingForm(request.POST, instance=tin)
        if tinform.is_valid():
            tinform.save()
            print("Form Saved")
        else:
            print("Form Error: ", tinform.errors)
    context = {'tin': tin, 'tinform': tinform}
    return render(request, 'Pages/tinedit.html', context)


@login_required
def EarEditPage(request):
    ear = EarPage.objects.all()[0]
    earform = EarPForm(instance=ear)
    if request.method == "POST":
        earform = EarPForm(request.POST, instance=ear)
        if earform.is_valid():
            earform.save()
            print("Form Saved")
        else:
            print("Form Error: ", earform.errors)
    context = {'ear': ear, 'earform': earform}
    return render(request, 'Pages/earedit.html', context)


@login_required
def ElecEditPage(request):
    electro = ElectroPage.objects.all()[0]
    electroform = ElectroForm(instance=electro)
    if request.method == "POST":
        electroform = ElectroForm(request.POST, instance=electro)
        if electroform.is_valid():
            electroform.save()
            print("Form Saved")
        else:
            print("Form Error: ", electroform.errors)
    context = {'electro': electro, 'electroform': electroform}
    return render(request, 'Pages/electroedit.html', context)


@login_required
def ManEditPage(request):
    electro = ManPage.objects.all()[0]
    electroform = ManForm(instance=electro)
    if request.method == "POST":
        electroform = ManForm(request.POST, instance=electro)
        if electroform.is_valid():
            electroform.save()
            print("Form Saved")
        else:
            print("Form Error: ", electroform.errors)
    context = {'electro': electro, 'electroform': electroform}
    return render(request, 'Pages/manedit.html', context)


@login_required
def MassageEditPage(request):
    electro = MassagePage.objects.all()[0]
    electroform = MassageForm(instance=electro)
    if request.method == "POST":
        electroform = MassageForm(request.POST, instance=electro)
        if electroform.is_valid():
            electroform.save()
            print("Form Saved")
        else:
            print("Form Error: ", electroform.errors)
    context = {'electro': electro, 'electroform': electroform}
    return render(request, 'Pages/massageedit.html', context)


@login_required
def ContactUsEditPage(request):
    contact = ContactUsPage.objects.all()
    context = {'contact': contact}
    return render(request, 'Pages/contact.html', context)


@login_required
def ShowContactPage(request, id):
    data = ContactUsPage.objects.get(id=id)
    form = ContactForm(instance=data)
    context = {'data': data, 'form': form}
    return render(request, 'Pages/viewContactForm.html', context)