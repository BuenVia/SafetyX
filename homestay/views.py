from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, LoginForm, PropertyForm
from .models import Property

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        return render(request, 'homestay/index.html')

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    context = {'registerform': form}
    return render(request, 'homestay/register.html', context=context)


def login(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        form = LoginForm()
        if request.method == "POST":
            form = LoginForm(request, data=request.POST)
            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    return redirect("dashboard")
        context = {'loginform': form}
        return render(request, 'homestay/login.html', context=context)

def logout(request):
    auth.logout(request)
    return redirect("index")

@login_required(login_url="login")
def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'homestay/dashboard.html', {'username': request.user.username})

@login_required(login_url="login")
def account(request):
    if request.user.is_authenticated:
        properties = Property.objects.filter(owner_id=request.user).all()
        context = {}
        context['user'] = request.user
        context['properties'] = properties
        return render(request, 'homestay/account.html', context=context)
    
@login_required
def property_create(request):
    if request.user.is_authenticated:
        context = {}
        form = PropertyForm()
        if request.method == "POST":
            form = PropertyForm(request.POST)
            if form.is_valid():
                new_property = form.save(commit=False)
                new_property.owner_id = request.user
                new_property.save()
                return redirect("dashboard")
        context['propertyForm'] = form
        context['user'] = request.user
        return render(request, 'homestay/property-create.html', context=context)
    