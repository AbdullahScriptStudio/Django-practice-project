from django.contrib import admin
from .models import User_model, UserInfoModel

# Register your models here.
admin.site.register(User_model)
admin.site.register(UserInfoModel)
