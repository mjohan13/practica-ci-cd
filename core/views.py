from django.http import HttpResponse

def home(request):
    return HttpResponse("¡Hola desde CI\CD con Django y Docker!")

# Create your views here.
