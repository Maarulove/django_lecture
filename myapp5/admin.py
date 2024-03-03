from django.contrib import admin
from .models import Product, Cattegory
# Register your models here.


@admin.action(description="Reset amount to zero")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'cattegory', 'quantity']
    ordering = ["cattegory", "-quantity"]
    list_filter = ["date_added", "price"]
    search_fields = ['description']
    search_help_text = ' search by description of product'
    actions = [reset_quantity]

    # fields = ['name', 'cattegory', 'description', 'date_added', 'rating', 'price']# this field is not good with fieldset

    readonly_fields = ['date_added', 'rating']
    fieldsets = [
        (None,{
            'classes':['wide'],
            'fields': ['name'],
        },),
        ("more",{
            'classes': ['collapse'],
            'description': 'Cattegory of products',
            'fields': ['cattegory', 'description']
        }),
        ('Accounting',{
            'fields': ['price', 'quantity'],
        }),
        (
            'rating and etc',{
                'description': "ratign and some other staff",
                'fields': ['rating', 'date_added']
            }
        ),

    ]

admin.site.register(Product, ProductAdmin)
admin.site.register(Cattegory)