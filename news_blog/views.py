from django.http import HttpResponse
from django.shortcuts import render
from .models import MyModel

def text_response_view(request):
    return HttpResponse("This is a text response")

def model_objects_view(request):
    objects = MyModel.objects.all()
    response = ", ".join([str(obj) for obj in objects])
    return HttpResponse(f"Model objects: {response}")

def template_view(request):
    objects = MyModel.objects.all()
    return render(request, 'myapp/template_view.html', {'objects': objects})
# Create your views here.
