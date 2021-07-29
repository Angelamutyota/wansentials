from django.shortcuts import render, redirect
from .forms import CreateUserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Order, Product, Profile
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404


# Create your views here.
def index(request):
    products = Product.objects.all
    context = {
        'products':products   
    }
    return render(request, 'index.html', context)

def registerPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginpage') 
        name = form.cleaned_data.get("username")
        messages.success(request, 'Account was created for' , name)
    context = {'form':form, 'profile':profile}
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'Incorrect Username or Password')
    context = {}
    return render(request, 'accounts/login.html', context)

def logoutpage(request):
    logout(request)
    return redirect('loginpage')


def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    user = request.user
    if request.method == 'POST':
        prof_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if prof_form.is_valid():
            prof_form.save()
            return redirect(request.path_info)
    else:
        prof_form = ProfileForm(instance=request.user.profile)
    profiles = Profile.objects.filter(user=user)
    context = {
        'profiles': profiles,
        'prof_form': prof_form,
    }
    return render(request, 'profile.html', context)

def update_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    if request.method == 'POST':
            prof_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
            if prof_form.is_valid():
                prof_form.save()
                return redirect('profile')
    else:
        prof_form = ProfileForm(instance=request.user.profile)
        context = {
            'prof_form': prof_form,
        }
    return render(request, 'updateprofile.html', context)

def search_results(request):

    if 'product' in request.GET and request.GET["product"]:
        search_term = request.GET.get("product")
        searched_products = Product.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"products": searched_products})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
        
def product(request, id):
    try:
        product = Product.objects.get(id =id)
    except ObjectDoesNotExist:
        raise Http404()

    return render(request, "product.html", {"product":product})

def checkout(request):

    if request.method == "POST":
        items = request.POST.get('items', "")
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zipcode = request.POST.get('zipcode', "")

        order = Order (name=name, email=email, address=address, city=city, state=state, zipcode= zipcode, items=items)
        order.save()

    return render(request, 'checkout.html')