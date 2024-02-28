from django.contrib import admin

from .models import Child, Task

admin.site.register(Child)
admin.site.register(Task)