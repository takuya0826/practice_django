from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(group_mst)
admin.site.register(user_mst)
admin.site.register(group_organaization)
admin.site.register(dir_mst)
admin.site.register(access_mst_user)
admin.site.register(access_mst_group)