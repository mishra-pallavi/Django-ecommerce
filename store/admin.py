from django.contrib import admin
from .models import Product,Variation, ReviewRating, ProductGallery
import admin_thumbnails
from django.utils.html import format_html
# Register your models here.


@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name','slug','category','price','stock','is_available','created_date','updated_date')
    inlines = [ProductGalleryInline]


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product','variation_category','variation_value','is_active','created_date','updated_date')
    list_editable = ('is_active',)
    list_filter = ('product','variation_category','variation_value','is_active')


@admin_thumbnails.thumbnail('image')
class ProductGalleryImageList(admin.ModelAdmin):
    def productImg(self, object):
        return format_html('<img src="{}" width=50 style="border-radius:10%;">'.format(object.image.url))
    productImg.short_description = "Product Image"


    model = ProductGallery     
    list_display = ('productImg','product')

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery,ProductGalleryImageList)