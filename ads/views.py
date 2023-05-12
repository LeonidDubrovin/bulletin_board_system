from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Count

# from .forms import PostAdsForm
# from django.contrib.auth.forms import User
# from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail

from ads.models import Author


@login_required(login_url='login')
def post_ads(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        phone = request.POST.get('phone')
        video = request.POST.get('video')
        file_count = request.POST.get('file_count')

        category_row = request.POST.get('category')
        category_check = Category.objects.filter(category_name=category_row).exists()
        if category_check:
            category = Category.objects.get(category_name=category_row)
        else:
            category = Category.objects.create(category_name=category_row)

        city_row = request.POST.get('city')
        city_check = City.objects.filter(city_name=city_row).exists()
        if city_check:
            city = City.objects.get(city_name=city_row)
        else:
            city = City.objects.create(city_name=city_row)

        ad = Ads.objects.create(author=request.user.author, title=title,
                                 description=description, price=price,
                                 category=category, city=city, phone=phone, video=video)

        # for file_num in range(0, int(file_count)):
        #     AdsImages.objects.create(
        #         ads=ad,
        #         image=request.FILES.get(f'images{file_num}')
        #     )

        # send email to admin
        mail_subject = "Новое абъявление добавлено"
        sender_email = request.user.email
        message = f"Новый запрос на модерацию от {sender_email}"
        print(message)
        to_email = settings.EMAIL_HOST_USER
        to_list = [to_email]
        from_email = settings.EMAIL_HOST_USER

        send_mail(
            mail_subject,
            message,
            from_email,
            to_list,
            fail_silently=False,
        )

    return render(request, 'ads/post-ads.html')


def ads_listing(request):
    ads_listing = Ads.objects.all()
    category_listing = Category.objects.annotate(
        total_ads=Count('ads')).order_by('category_name')

    context = {
        'ads_listing': ads_listing,
        'category_listing': category_listing
    }

    return render(request, 'ads/ads-listing.html', context)


def ads_detail(request, pk):
    ads_detail = get_object_or_404(Ads, pk=pk)
    ads_photos = AdsImages.objects.filter(ads=ads_detail)

    context = {
        'ads_detail': ads_detail,
        'ads_photos': ads_photos,
    }

    return render(request, 'ads/ads-detail.html', context)


def ads_category_archive(request, slug):
    category = get_object_or_404(Category, slug=slug)
    ads_by_category = Ads.objects.filter(category=category)

    context = {
        'category': category,
        'ads_by_category': ads_by_category
    }

    return render(request, 'ads/category-archive.html', context)


def ads_region_archive(request, slug):
    region = get_object_or_404(Region, slug=slug)
    ads_by_region = Ads.objects.filter(region=region)

    context = {
        'region': region,
        'ads_by_region': ads_by_region
    }

    return render(request, 'ads/region-archive.html', context)


def ads_city_archive(request, slug):
    city = get_object_or_404(City, slug=slug)
    ads_by_city = Ads.objects.filter(city=city)

    context = {
        'city': city,
        'ads_by_city': ads_by_city
    }

    return render(request, 'ads/city-archive.html', context)


def ads_author_archive(request, pk):
    author = get_object_or_404(Author, pk=pk)
    ads_by_author = Ads.objects.filter(author=author)

    context = {
        'author': author,
        'ads_by_author': ads_by_author
    }

    return render(request, 'ads/author-archive.html', context)


def ads_search(request):
    region = request.GET.get('region_name')
    category = request.GET.get('category_name')

    if region:
        ads_search_result = Ads.objects.filter(region__region_name=region)
    elif category:
        ads_search_result = Ads.objects.filter(category__category_name=category)
    else:
        ads_search_result = Ads.objects.filter(region__region_name=region).filter(
            category__category_name=category)

    context = {
        'ads_search_result': ads_search_result
    }

    return render(request, 'ads/ads-search.html', context)


@login_required(login_url='login')
def ads_delete(request, pk):
    ad = get_object_or_404(Ads, pk=pk)
    ad.delete()
    return redirect("dashboard")









