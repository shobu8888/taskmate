from django.shortcuts import render , redirect
from django.contrib import messages
from .forms import RegisterFrom

def register(request):
    if request.method == "POST":
        register_form = RegisterFrom(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("Account Created!!!"))
            return redirect('register')
        else:
            return render(request,'register.html',{'register_form':register_form} )
    else:
        register_form = RegisterFrom
        return render(request,'register.html',{'register_form':register_form} )
