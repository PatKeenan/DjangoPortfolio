from django.contrib import admin
from .models import *

admin.site.register(Language)
admin.site.register(BlogPost)
# Register your models here.
admin.site.register(Project)
admin.site.register(Category)

