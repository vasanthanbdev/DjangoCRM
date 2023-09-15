from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

def home(request):
    records = Record.objects.all()
    
    #if user is trying to log in 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        #authentication
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Successfully Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Loggin You In, Please Try Again...")
            return redirect('home')
    else:
        return render(request, "home.html", {"records": records})

# def log_in(request):
#     pass

def log_out(request):
    logout(request)
    messages.success(request, "You Have Been Successfully Logged Out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and login
            username = form.changed_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Been Registered Successfully...")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, "register.html", {'form': form})
    
def customer_record(request, pk):
    if request.user.is_authenticated :
        customer_record = Record.objects.get(id=pk)
        return render(request, "record.html", {"customer_record": customer_record})
    else:
        messages.success(request, "You are not logged in...")
        return redirect('home')