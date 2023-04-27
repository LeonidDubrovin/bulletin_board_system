from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default="default-profile-pic.png",
                                    upload_to='uploads/profile-pictures',
                                    null=True)
    class Meta:
        verbose_name_plural = "Авторы"

    def __str__(self):
        return self.user.username


class Ads(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = RichTextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    # dormitory = models.ForeignKey('Dormitory', on_delete=models.CASCADE, null=True)
    region = models.ForeignKey('Region', on_delete=models.CASCADE, null=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=50)
    video = EmbedVideoField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.title


class Region(models.Model):
    region_name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.region_name:
            self.slug = slugify(self.region_name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Регионы"

    def __str__(self):
        return self.region_name


class City(models.Model):
    city_name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.city_name:
            self.slug = slugify(self.city_name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Города"

    def __str__(self):
        return self.city_name


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to='uploads/category', blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.category_name:
            self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.category_name


class AdsImages(models.Model):
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d', default=None)

    def __str__(self):
        return self.ads.title

    class Meta:
        verbose_name_plural = 'Изображения объявлений'
