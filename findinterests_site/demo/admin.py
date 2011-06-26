from django.contrib import admin
from models import *

class FacebookUserAdmin(admin.ModelAdmin):
    list_display = ('uid',)

admin.site.register(FacebookUser, FacebookUserAdmin)