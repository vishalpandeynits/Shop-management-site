from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Employee)
admin.site.register(Shop)
admin.site.register(Item)
admin.site.register(IssueItem)
admin.site.register(Note)