from django.contrib import admin

from catalog.models import Tumb


@admin.register(Tumb)
class TumbAdmin(admin.ModelAdmin):
    pass
