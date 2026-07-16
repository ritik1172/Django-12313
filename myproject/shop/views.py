from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "shopHome.html")

def contact(request):
    return render(request, "shopContact.html")