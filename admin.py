from django.contrib import admin
from .models import Catagory,Product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','description')
admin.site.register(Catagory,CategoryAdmin)
admin.site.register(Product)



