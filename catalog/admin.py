from django.contrib import admin
from .models import Category, Producer, Product


admin.site.register(Category)
admin.site.register(Producer)
admin.site.register(Product)



# from django.contrib import admin
# from modeltranslation.admin import TranslationAdmin
# from .models import Category, Producer, Product


# @admin.register(Category)
# class Category(TranslationAdmin):
#     list_display = ('name',)
#     list_display_links = ('name',)


# @admin.register(Producer)
# class Producer(TranslationAdmin):
#     list_display = ('name',)
#     list_display_links = ('name',)


# @admin.register(Product)
# class Product(TranslationAdmin):
#     list_display = ('name', 'description', 'price', 'first_price', 'quantity', 'photo', 'category', 'producer')
#     list_display_links = ('name', )