from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from django.shortcuts import get_object_or_404

def contact_form(request):
    return render(request, "contact.html");

def submit_form(request):
    if request.method == "POST":
        name = request.POST.get("name");
        email = request.POST.get("email");
        age = request.POST.get("age");
        if name and email:
            Student.objects.create(name=name, email=email, age=age);
            return HttpResponse(f"thanks {name} for saving the data...");
        else:
            return HttpResponse("All fields should be filled...")
    return redirect('contact_form');

def details(request):
    students = Student.objects.all();
    return render(request, "details.html", {"students": students});

def delete_student(request, id):
    student = get_object_or_404(Student, id=id);
    student.delete();
    return redirect("details")

def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    
    if request.method == "POST":
        student.name = request.POST.get("name");
        student.email = request.POST.get("email");
        student.age = request.POST.get("age");
        
        student.save();
        return redirect("details");
    return render(request, "update.html", {"student": student})