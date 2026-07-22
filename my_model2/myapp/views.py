from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student


# Registration Page
def contact_form(request):
    return render(request, "contact.html")


# Register User & Student
def submit_form(request):
    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not name or not email or not password:
            messages.error(request, "All fields are required.")
            return redirect("contact_form")

        # Check if user already exists
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("contact_form")

        # Create Django User
        User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        # Save Student Details
        Student.objects.create(
            name=name,
            email=email
        )

        messages.success(request, "Registration Successful!")
        return redirect("login")

    return redirect("contact_form")


# Login
def login_page(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful!")
            return redirect("details")

        messages.error(request, "Invalid Email or Password")

    return render(request, "login.html")


# Logout
def logout_page(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect("login")


# Display Students
@login_required(login_url="login")
def details(request):

    students = Student.objects.all()

    return render(request, "details.html", {
        "students": students
    })


# Delete Student
@login_required(login_url="login")
def delete_student(request, id):

    student = get_object_or_404(Student, id=id)

    student.delete()

    messages.success(request, "Student Deleted Successfully!")

    return redirect("details")


# Update Student
@login_required(login_url="login")
def update_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == "POST":

        student.name = request.POST.get("name")
        student.email = request.POST.get("email")

        student.save()

        messages.success(request, "Student Updated Successfully!")

        return redirect("details")

    return render(request, "update.html", {
        "student": student
    })