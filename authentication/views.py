from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, \
    Http404
# importing messages
from django.contrib import messages
# import authentication related stuffs
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import User

from ads.models import Author
from .forms import UserRegistrationForm

from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .tokens import account_activation_token


def signup_view(request):
    if request.method == 'POST':
        reg_form = UserRegistrationForm(request.POST)

        if reg_form.is_valid():
            instance = reg_form.save(commit=False)
            instance.is_active = False
            instance.save()

            author_check = Author.objects.filter(user=instance).exists()
            if not author_check:
                author = Author.objects.create(user=instance)


            site = get_current_site(request)
            mail_subject = "Активация аккаунта"
            message = render_to_string('authentication/confirm-email.html', {
                'user': instance,
                'domain': site.domain,
                'uid': instance.id,
                'token': account_activation_token.make_token(instance)
            })

            to_email = reg_form.cleaned_data.get('email')
            to_list = [to_email]
            from_email = settings.EMAIL_HOST_USER
            send_mail(mail_subject, message, from_email, to_list,
                      fail_silently=False, )

            return redirect('signup-success')

            # url_activate = f"http://{site.domain}/activate/{instance.id}/{account_activation_token.make_token(instance)}/"
            # context = {
            #     'user': instance,
            #     'domain': site.domain,
            #     'uid': instance.id,
            #     'token': account_activation_token.make_token(instance)
            # }
            # return render(request, 'authentication/confirm-email.html', context)

    else:
        reg_form = UserRegistrationForm()

    context = {
        'reg_form': reg_form,
    }

    return render(request, 'authentication/signup.html', context)


def signup_success_view(request):
    return render(request, 'authentication/signup-success.html')


def account_activate_view(request, uid, token):
    try:
        user = get_object_or_404(User, pk=uid)
    except:
        raise Http404("No User found")

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'authentication/activate-account.html')
    else:
        return HttpResponse("Ссылка активации аккаунта невалидна.")


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect_url = request.GET.get('next', 'home')
            return redirect(redirect_url)
        else:
            messages.error(request,
                           f"Oops! Username or Password is invalid. Please try again.")

    return render(request, 'authentication/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
