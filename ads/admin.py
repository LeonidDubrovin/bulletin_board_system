from django.contrib import admin
from .models import Author, Ads, Region, City, Category, AdsImages


class AdsImagesStakedInlineAdmin(admin.StackedInline):
    model = AdsImages


class AdsImagesAdmin(admin.ModelAdmin):
    pass


class AdsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'price', 'author', 'category', 'date_created',
        'is_featured',
        'is_active')

    list_display_links = ('id', 'title')
    list_editable = ('is_featured', 'is_active')
    search_fields = ('title', 'price', 'region', 'category')
    list_filter = ('price', 'date_created', 'region', 'is_featured')
    inlines = [AdsImagesStakedInlineAdmin]


admin.site.register(Ads, AdsAdmin)
admin.site.register(AdsImages, AdsImagesAdmin)
admin.site.register(Author)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(Category)
