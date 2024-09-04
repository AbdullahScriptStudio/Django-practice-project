from django.contrib import admin
from .models import Topic, Product, accessrecord, webpage
# Register your models here.

admin.site.register(Topic)
admin.site.register(webpage)
admin.site.register(accessrecord)
admin.site.register(Product)
