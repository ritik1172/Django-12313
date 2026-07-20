from django.shortcuts import render, redirect
from django.http import HttpResponse;
from .models import Student

# Create your views here.
def contact_form(request):
    return render(request, "contact.html")

def submit_form(request):
    if request.method == "POST":
        name = request.POST.get("name");
        email = request.POST.get("email");
        age = request.POST.get("age");
        
        if name and email:
            Student.objects.create(name=name, email=email, age=age);
            return HttpResponse(f"thanks {name} for saving this form...");
        else:
            return HttpResponse("All field should be filled...")
    return redirect('contact_form')
        
        