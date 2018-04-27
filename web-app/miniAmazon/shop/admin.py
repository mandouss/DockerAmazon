from django.contrib import admin

from .models import Category, Good, Stock, Aorder, Uorder, Warehouse

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class GoodAdmin(admin.ModelAdmin):
    list_display = ['ID', 'description', 'available', 'created', 'updated',]
    list_editable = ['available']
    prepopulated_fields = {'slug':('description',)}
    list_per_page = 20
admin.site.register(Good, GoodAdmin)

class StockAdmin(admin.ModelAdmin):
    list_display = ['whid', 'amount', ]

class AorderAdmin(admin.ModelAdmin):
    list_display = ['ordernum', 'ID', 'description', 'amount', 'whid', 'desx', 'desy','email']

class WarehouseAdmin(admin.ModelAdmin):
    list_display=['whid', 'x', 'y', ]

admin.site.register(Stock, StockAdmin)

admin.site.register(Aorder, AorderAdmin)
admin.site.register(Uorder)
admin.site.register(Warehouse, WarehouseAdmin)
# Register your models here.
