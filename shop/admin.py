from django.contrib import admin
from .models import Contact, Category, Product, Feature, Type, ProductImage, About


@admin.register(Contact)
class Admin(admin.ModelAdmin):
    pass


@admin.register(Category)
class Admin(admin.ModelAdmin):
    pass


@admin.register(Feature)
class Admin(admin.ModelAdmin):
    pass


@admin.register(Type)
class Admin(admin.ModelAdmin):
    pass


@admin.register(Product)
class Admin(admin.ModelAdmin):
    pass


@admin.register(ProductImage)
class Admin(admin.ModelAdmin):
    pass


@admin.register(About)
class Admin(admin.ModelAdmin):
    pass
