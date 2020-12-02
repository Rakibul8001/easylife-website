from django.contrib import admin
from .models import Product, ProductImage,Variation

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    list_display = ['__str__','title','price','slug','updated','active']
    search_fields = ['title','description','price']
    list_editable = ['price','active']
    list_filter = ['price', 'active']
    readonly_fields = ['updated','timestamp']
    prepopulated_fields = {"slug":("title",)}
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Variation)