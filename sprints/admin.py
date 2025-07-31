from django.contrib import admin
from .models import Sprint, Epic, Story, Task, AcceptanceCriteria

# Register your models here.

admin.site.register(Sprint)
admin.site.register(Epic)
admin.site.register(Story)
admin.site.register(Task)
admin.site.register(AcceptanceCriteria)