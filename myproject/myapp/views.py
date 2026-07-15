from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Home of myapp...")

def about(request):
    return HttpResponse("About of myapp...")