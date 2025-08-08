from django.contrib import admin
from .models import Sprint, Story, Task, AcceptanceCriteria

# Register your models here.

@admin.register(Sprint)
class SprintAdmin(admin.ModelAdmin):
    list_display = ("title", "start_date", "end_date")
    search_fields = ("title",)
    ordering = ("start_date",)


@admin.register(AcceptanceCriteria)
class CriteriaAdmin(admin.ModelAdmin):
    list_display = ("title", "story", "status")
    list_filter = ("status",)
    search_fields = ("title",)
    ordering = ("story",)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "story", "status")
    list_filter = ("status",)
    search_fields = ("title",)
    ordering = ("story",)


# Inline for Task
class TaskInline(admin.TabularInline):
    model = Task
    extra = 1  # Show one empty form by default
    fields = ("title", "description", "status", "created_on", "updated_on")
    readonly_fields = ("created_on", "updated_on")
    show_change_link = True  # Optional: lets you click through to full Task edit page

# Inline for AcceptanceCriteria
class AcceptanceCriteriaInline(admin.TabularInline):
    model = AcceptanceCriteria
    extra = 1
    fields = ("title", "description", "status", "created_on", "updated_on")
    readonly_fields = ("created_on", "updated_on")
    show_change_link = True

# Story admin with inlines
@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ("title", "epic", "status", "updated_on")
    list_filter = ("status", "epic__sprint")
    search_fields = ("title", "description")
    readonly_fields = ("created_on", "updated_on")
    inlines = [TaskInline, AcceptanceCriteriaInline]