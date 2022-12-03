from django.contrib import admin

from .models import Contact, Producto


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'second_name', 'first_last_name', 'second_last_name')
    list_display = ('first_name', 'second_name', 'first_last_name', 'second_last_name', 'email_adress',
    'full_phone_number', 'comment')
    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
    search_fields = ('name',)


admin.site.register(Contact, ContactAdmin)
admin.site.register(Producto, ProductoAdmin)