from django.shortcuts import render
from .models import CarBrand
# Create your views here.
def index(request):
    brand=CarBrand.objects.all()
    return render(request,'index.html',{'brand':brand})