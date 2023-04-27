from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from authentication.forms import UserUpdateForm, ProfileUpdateForm


@login_required(login_url='login')
def profile_dashboard(request):
    ads_posted = request.user.author.ads_set.all()
    total_ads = request.user.author.ads_set.all().count()
    featured_ads = request.user.author.ads_set.filter(is_featured=True).count()

    context = {
        'ads_posted': ads_posted,
        'total_ads': total_ads,
        'featured_ads': featured_ads
    }
    return render(request, 'profiles/account-dashboard.html', context)


@login_required(login_url='login')
def profile_settings(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.author)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f"Your profile has been updated successfully!")
            return redirect('profile-settings')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.author)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'profiles/account-setting.html', context)


@login_required(login_url='login')
def profile_ads(request):
    return render(request, 'profiles/all-ads.html')


@login_required(login_url='login')
def profile_favorite_ads(request):
    return render(request, 'profiles/favourite-ads.html')
