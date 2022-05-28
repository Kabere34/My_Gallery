from django.contrib import admin
from .models import Images,Category,Location

# Register your models here.class ImageAdmin(admin.ModelAdmin):

admin.site.register(Images)
admin.site.register(Category)
admin.site.register(Location)
