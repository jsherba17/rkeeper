from django.contrib import admin

from cafe.models import *

admin.site.register(Order)
admin.site.register(Staff)
admin.site.register(Food)
admin.site.register(Quantity)
admin.site.register(Table)