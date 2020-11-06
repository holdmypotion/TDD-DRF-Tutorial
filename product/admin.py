from django.contrib import admin

from .models import Product, Section

class ProductAdmin(admin.ModelAdmin):
    """Extra functionalities on the admin interface"""
    search_fields = ['title', 'description', 'section']
    list_display = ['title', 'section', 'active', 'update']
    list_editable = ['active', 'section']
    list_filter = ['section', 'active']
    readonly_fields = ['timestamp', 'update']
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(Section)