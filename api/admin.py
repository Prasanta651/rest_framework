from django.contrib import admin

from api.models import Order
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    raw_id_fields = ("user",)
    list_display = [field.attname for field in Order._meta.fields]


admin.site.register(Order, OrderAdmin)