from django.contrib import admin

# Register your models here.
from .models import Good

class GoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'slug']
    class Meta:
        model = Good

admin.site.register(Good, GoodAdmin)
