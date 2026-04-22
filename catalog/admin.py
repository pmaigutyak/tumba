from django.contrib import admin

from catalog.models import Tumb, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tumb)
class TumbAdmin(admin.ModelAdmin):
    pass
