from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import SingupForm, UserForm, ProfileForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import authenticate, login


def signup(request):
    if request.method == 'POST':
        form = SingupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/accounts/profile')
    else:
        form = SingupForm()
    context = {'form':form}
    return render(request, "registration/signup.html", context)

#   PROFILE FORM 
def profile(request):
    profile_page = Profile.objects.get(user = request.user)
    context = {'profile_page': profile_page}
    return render(request, 'profile/profile.html', context)

#   PROFILE EDIT FORM 
def profile_edit(request):
    profile_edit = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=profile_edit)
        #   SAVE DATA 
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            my_profile = profile_form.save(commit=False)
            my_profile.user = request.user
            my_profile.save()
            return redirect('/accounts/profile')

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile_edit)
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'profile/profile_edit.html', context)

