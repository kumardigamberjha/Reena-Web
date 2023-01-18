from django.shortcuts import render

def EditPages(request):
    context = {}
    return render(request, 'EditPages/editpage.html', context)