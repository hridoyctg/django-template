from django.contrib import admin
from django.contrib.admin.sites import site
from .models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'age',
        'description',
        'image'
    ]


admin.site.register(Profile, ProfileAdmin)
