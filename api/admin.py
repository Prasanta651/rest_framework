from django.contrib import admin

from api.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
class OrderAdmin(admin.ModelAdmin):
    inlines = [ OrderItemInline ]
    raw_id_fields = ("user",)
    list_display = [field.attname for field in Order._meta.fields]


admin.site.register(Order, OrderAdmin)