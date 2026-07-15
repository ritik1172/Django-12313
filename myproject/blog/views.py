from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Home of blog...")

def about(request):
    return HttpResponse("About of blog...")