from django.shortcuts import render
from ads.models import Ads, Region, Category


def home(request):
    recent_ads = Ads.objects.filter(is_active=True).order_by('date_created')[0:3]
    featured_ads = Ads.objects.filter(is_featured=True).filter(is_active=True)
    category_listing = Category.objects.all()
    region_listing = Region.objects.all()

    region_search = Region.objects.values_list('region_name', flat=True).distinct().order_by("region_name")
    category_search = Category.objects.values_list('category_name', flat=True).distinct().order_by("category_name")

    context = {
        'recent_ads': recent_ads,
        'featured_ads': featured_ads,
        'region_search': region_search,
        'category_search': category_search,
        'category_listing': category_listing,
        'region_listing': region_listing,
    }

    return render(request, 'pages/index.html', context)


def faq(request):
    return render(request, 'pages/faq.html')


def terms_of_service(request):
    return render(request, 'pages/terms-of-service.html')


def contact(request):
    return render(request, 'pages/contact.html')
