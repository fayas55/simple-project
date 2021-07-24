from django.shortcuts import render
from django.http import HttpResponse
from .models import Editor
from .forms import Formeditor

# Create your views here.
def index(request):
    form = Formeditor()
    return render(request,'index.html',{'form':form})
