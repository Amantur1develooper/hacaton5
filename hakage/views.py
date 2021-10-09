from django.shortcuts import render
from django.shortcuts import render ,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .models import products

# Create your views here.
from django.shortcuts import render

# Create your views here.

def base(request):
    product=products.objects.all()
    return render(request, 'index.html',{'product':product})
  
def contact(request):
    return render(request, 'contact.html')
def detail(request):
    return render(request, 'shop-details.html')
def cart(request):
    return render(request, 'shoping-cart.html')


def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=UserCreationForm()
    return render(request,'adduser.html',{'form':form})