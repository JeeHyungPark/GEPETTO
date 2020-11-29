from django.contrib import admin
from .models import *


class TestAdmin(admin.ModelAdmin):

    list_display = (
        'tester',
        'text',
        'test_probability',
    )
admin.site.register(Test, TestAdmin)
