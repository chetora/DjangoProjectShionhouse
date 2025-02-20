from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
admin.site.site_header = "ACLEDA University of Business"
admin.site.site_title = "ACLEDA University of Business Admin Panel"
admin.site.index_title = "ACLEDA Admin Panel"

class CustomerAdmin(admin.ModelAdmin):  
    list_display = ["id","name","phone","email","date_created"]
    list_filter = ["name","email","date_created"]
    search_fields = ["name","email"]
admin.site.register(Customer,CustomerAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["CategoryName","CategoryDate"]
    list_filter = ["CategoryName","CategoryDate"]
    search_fields = ["CategoryName"]
admin.site.register(Category,CategoryAdmin)

class SupplierAdmin(admin.ModelAdmin):
    list_display = ["companyName","phone","email","date_created"]
    list_filter = ["companyName","email","date_created"]
    search_fields = ["companyName","email"]
admin.site.register(Supplier,SupplierAdmin)

class ProductAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.productImage:
            return format_html('<img src="/static{}" style="width: 100px; height: auto;" />', obj.productImage.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'

    list_display = ["id","image_preview","productName","supplierID","categoryID","priceIn","priceOut","productDate"]
    list_filter = ["productDate","productName","priceOut"]
    search_fields = ["productName","priceOut"]
    date_hierarchy = "productDate"
    readonly_fields = ["image_preview"]

admin.site.register(tblProducts, ProductAdmin)

admin.site.register(ImageType)
admin.site.register(Image)