from django.contrib import admin
from .models import *


admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Theme)
admin.site.register(ThemeFile)
admin.site.register(ThemeVideoLink)
admin.site.register(ThemeImage)

