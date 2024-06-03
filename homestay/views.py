from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, LoginForm, PropertyForm
from .models import Property, Company, UserCompany

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        return render(request, 'homestay/index.html')

def register(request):
    user_form = CreateUserForm()
    if request.method == "POST":
        user_form = CreateUserForm(request.POST)
        if user_form.is_valid():
            ### The company object needs to be referenced in the UserCompany model.
            company = Company(name=None, phone=None, country=None)
            company.save()
            user_form.company_id = company
            user_form.save()
            user_company = UserCompany(user_id=user_form,company_id=company)
            user_company.save()
            return redirect("login")
    context = {}
    context['user_form'] = user_form
    # context['company_form'] = company_form
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
        ### The property then needs to be looked up by Company, not user
        user = request.user
        properties = Property.objects.filter(company_id=request.user, is_delete=False).all()
        context = {}
        context['username'] = request.user
        context['properties'] = properties
        return render(request, 'homestay/dashboard.html', context=context)

@login_required
def question_set(request, id):
    property = Property.objects.filter(id=id, is_delete=False).first()
    return render(request, 'homestay/question-set.html', {'property': property})

@login_required(login_url="login")
def account(request):
    if request.user.is_authenticated:
        properties = Property.objects.filter(company_id=request.user, is_delete=False).all()
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
                new_property.company_id = request.user
                new_property.save()
                return redirect("dashboard")
        context['propertyForm'] = form
        context['user'] = request.user
        return render(request, 'homestay/property-create.html', context=context)
    
@login_required
def property_edit(request, id):
    if request.user.is_authenticated:
        context = {}
        property = Property.objects.filter(id=id).first()
        form = PropertyForm(instance=property)
        if request.method == "POST":
            form = PropertyForm(request.POST, instance=property)
            if form.is_valid():
                update_property = form.save(commit=False)
                update_property.company_id = request.user
                update_property.save()
                return redirect("/homestay/dashboard")
            
        context['propertyForm'] = form
        context['id'] = id
        return render(request, 'homestay/property-edit.html', context=context)
    
@login_required
def property_delete(request, id):
    if request.user.is_authenticated:
        context = {}
        property = Property.objects.filter(id=id).first()
        if request.method == "POST" and request.POST.get('property_name') == property.name:
            property.is_delete = True
            property.save()
            return redirect('/homestay/dashboard')
        context['property'] = property
        context['id'] = id
        return render(request, 'homestay/property-delete.html', context=context)