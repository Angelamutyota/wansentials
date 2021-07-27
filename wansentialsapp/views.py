from django.shortcuts import render, redirect
from .forms import CreateUserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Profile


# Create your views here.
def index(request):
    return render(request, 'index.html',)

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
