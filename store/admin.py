from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product


admin.site.site_header = "Shirin's Boutique Admin"
admin.site.site_title = "Shirin's Boutique"
admin.site.index_title = "Product Management"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')
    list_select_related = ('category',)
    ordering = ('name',)

    def image_preview(self, product):
        if not product.image:
            return 'No image'

        return format_html(
            '<img src="{}" style="width: 56px; height: 70px; object-fit: cover; border-radius: 6px;" />',
            product.image.url,
        )

    image_preview.short_description = 'Image'
