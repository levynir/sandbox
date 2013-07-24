from django.contrib import admin
from cars.models import Car,CarModel,CarMaker

class CarModelAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['carmaker','name']}),
    ]
    list_display = ('carmaker','name')

class CarAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['carmodel','year','owners','pub_date']}),
    ]
    list_display = ('carmodel','year','owners')


admin.site.register(CarMaker)
admin.site.register(CarModel,CarModelAdmin)
admin.site.register(Car,CarAdmin)