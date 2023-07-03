from django.shortcuts import render
from Pages.models import DermaLogicaPage, Homepage, AboutUsPage, IPLPage, EarPage, ElectroPage, MakeUpPage, ManPage, MassagePage, CaciSynergyPage, GiftPage, NailPage, WaxingPage, TintingPage, NewPage, AddItemModel
from website.forms import DermaForm, HomeForm, AboutUsForm, CaciForm, IPLForm, WaxingForm, NailForm, MakeUpForm, TintingForm, EarPForm, ElectroForm, ManForm, MassageForm, ContactForm, NewPageForm, AddItemNewPageForm
from django.contrib.auth.decorators import login_required
from Booking.models import BookingModel
import datetime
from website.models import ContactUsPage, CartBookingModel

@login_required
def EditPageView(request):
    somemonth = datetime.date.today()
    months = somemonth.month
    todays_bookings_q = CartBookingModel.objects.filter(BookingTime__date=somemonth)
    todays_bookings = todays_bookings_q.count()
    todays_appointment_q = CartBookingModel.objects.filter(date=somemonth)
    todays_appointment = todays_appointment_q.count()
    monthly_appointment = CartBookingModel.objects.filter(BookingTime__month=months)
    monthly_appointment1 = CartBookingModel.objects.filter(BookingTime__month=1)
    monthly_appointment1_count = monthly_appointment1.count()
    print("1: ", monthly_appointment1)
    monthly_appointment2 = CartBookingModel.objects.filter(BookingTime__month=2)
    monthly_appointment2_count = monthly_appointment2.count()
    print("2: ", monthly_appointment2)
    monthly_appointment3 = CartBookingModel.objects.filter(BookingTime__month=3)
    monthly_appointment3_count = monthly_appointment3.count()
    print("3: ", monthly_appointment3)
    monthly_appointment4 = CartBookingModel.objects.filter(BookingTime__month=4)
    monthly_appointment4_count = monthly_appointment4.count()
    print("4: ", monthly_appointment4)
    monthly_appointment5 = CartBookingModel.objects.filter(BookingTime__month=5)
    monthly_appointment5_count = monthly_appointment5.count()
    print("5: ", monthly_appointment5_count)
    monthly_appointment6 = CartBookingModel.objects.filter(BookingTime__month=6)
    monthly_appointment6_count = monthly_appointment6.count()
    print("6: ", monthly_appointment6_count)
    monthly_appointment7 = CartBookingModel.objects.filter(BookingTime__month=7)
    monthly_appointment7_count = monthly_appointment7.count()
    print("7: ", monthly_appointment7)
    monthly_appointment8 = CartBookingModel.objects.filter(BookingTime__month=8)
    monthly_appointment8_count = monthly_appointment8.count()
    print("8: ", monthly_appointment8)
    monthly_appointment9 = CartBookingModel.objects.filter(BookingTime__month=9)
    monthly_appointment9_count = monthly_appointment9.count()
    print("9: ", monthly_appointment9)
    monthly_appointment10 = CartBookingModel.objects.filter(BookingTime__month=10)
    monthly_appointment10_count = monthly_appointment10.count()
    print("10: ", monthly_appointment10)
    monthly_appointment11 = CartBookingModel.objects.filter(BookingTime__month=11)
    monthly_appointment11_count = monthly_appointment11.count()
    print("11: ", monthly_appointment11)
    monthly_appointment12 = CartBookingModel.objects.filter(BookingTime__month=12)
    monthly_appointment12_count = monthly_appointment12.count()
    print("12: ", monthly_appointment12)
    jan = 0
    for i in monthly_appointment1:
        jan += int(i.total_payment)

    feb = 0
    for i in monthly_appointment2:
        feb += int(i.total_payment)

    mar = 0
    for i in monthly_appointment3:
        mar += int(i.total_payment)

    apr = 0
    for i in monthly_appointment4:
        apr += int(i.total_payment)

    may = 0
    for i in monthly_appointment5:
        may += int(i.total_payment)

    june = 0
    for i in monthly_appointment6:
        june += int(i.total_payment)

    july = 0
    for i in monthly_appointment7:
        july += int(i.total_payment)

    aug = 0
    for i in monthly_appointment8:
        aug += int(i.total_payment)

    sep = 0
    for i in monthly_appointment9:
        sep += int(i.total_payment)

    oct1 = 0
    for i in monthly_appointment10:
        oct1 += int(i.total_payment)

    nov = 0
    for i in monthly_appointment11:
        nov += int(i.total_payment)

    dec = 0
    for i in monthly_appointment12:
        dec += int(i.total_payment)

    print("Jan: ", jan, 'Feb: ', feb, 'mar', mar, 'apr: ', apr, 'may: ', may, 'june: ', june, 'july: ', july, 'aug: ', aug,'sep:', sep, 'oct: ', oct1, 'nov: ', nov, 'dec: ', dec)

    mac = monthly_appointment.count()
    tb6 = todays_bookings_q[:20]
    ta6 = todays_appointment_q[:20]
    print("todays_bookings: ", todays_bookings)
    print("todays_appointment: ", todays_appointment)

    total = 0
    for i in monthly_appointment:
        total += int(i.total_payment)

    context = {'todays_bookings': todays_bookings, 'todays_appointment': todays_appointment, 'monthly_appointment': monthly_appointment, 'mac': mac, 'total': total, 'todays_bookings_q':todays_bookings_q, 'todays_appointment_q':todays_appointment_q, 'ta6': ta6, 'tb6': tb6, "Jan": jan, 'Feb':  feb, 'mar': mar, 'apr': apr, 'may': may, 'june': june, 'july': july, 'aug': aug,'sep': sep, 'oct': oct1, 'nov': nov, 'dec': dec}
    return render(request, 'Pages/editpage.html', context)

@login_required
def HomePageView(request):
    home = Homepage.objects.all()[0]
    homeform = HomeForm(instance=home)
    if request.method == "POST":
        homeform = HomeForm(request.POST, request.FILES, instance=home)
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
        aboutform = AboutUsForm(request.POST, request.FILES, instance=about)
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
        dermaform = DermaForm(request.POST, request.FILES, instance=derma)
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
        caciform = CaciForm(request.POST, request.FILES, instance=caci)
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
        iplform = IPLForm(request.POST, request.FILES, instance=ipl)
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
        waxform = WaxingForm(request.POST, request.FILES, instance=wax)
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
        nailform = NailForm(request.POST, request.FILES, instance=nail)
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
        makeform = MakeUpForm(request.POST, request.FILES, instance=make)
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
        tinform = TintingForm(request.POST, request.FILES, instance=tin)
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
        earform = EarPForm(request.POST, request.FILES, instance=ear)
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
        electroform = ElectroForm(request.POST, request.FILES, instance=electro)
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
        electroform = ManForm(request.POST, request.FILES, instance=electro)
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
        electroform = MassageForm(request.POST, request.FILES, instance=electro)
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


# def NewPageView(request):
#     form = NewPageForm()

#     if request.method == 'POST':
#         form = NewPageForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print("Form Saved")
#         else:
#             print("Form Error: ", form.errors)
    
#     return render(request, 'Pages/newpage.html', {'form': form})


def NewPageView(request):
    form1 = NewPageForm()
    form2 = AddItemNewPageForm()
    
    if request.method == "POST":
        form1 = NewPageForm(request.POST)
        content = request.POST.get('content')
        print('content: ', content)
        if form1.is_valid():
            ss = form1.save()
            print("SS id: ", ss.id)

            print("Form Saved")

        else:
            print("Form Error: ", form1.errors)
        name = request.POST.get('name')
        content = request.POST.get('content')
        new_page = NewPage.objects.get(id=ss.id)
        form23 = AddItemModel(entry_instance=new_page, content=content)
        sd = form23.save()
        print("Form2 Saved: ", sd)

    context = {'form2': form2}
       
    return render(request, 'Pages/newpage.html', context)


def ShowNewPage(request, id):
    data = NewPage.objects.get(id=id)
    pagedata = AddItemModel.objects.filter(entry_instance=data.id)
    print("page Data: ", pagedata)
    print("data: ", data)
    context = {'data': data}
    return render(request, 'Pages/show_new_page.html', context)