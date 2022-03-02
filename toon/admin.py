from django.contrib import admin

# Register your models here.

from .models import Toon, Days

admin.site.register(Toon)


class DaysAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('day',)}

admin.site.register(Days, DaysAdmin)