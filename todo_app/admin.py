from django.contrib import admin
from .models import Task, TimeHorizon, TaskStatus, User, Counter

admin.site.register(Task)
admin.site.register(TimeHorizon)
admin.site.register(TaskStatus)
admin.site.register(User)
admin.site.register(Counter)
