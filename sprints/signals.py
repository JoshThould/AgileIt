from .models import Story, Task, AcceptanceCriteria
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Task, AcceptanceCriteria

@receiver([post_save, post_delete], sender=Task)
def update_story_status_from_task(sender, instance, **kwargs):
    if instance.story:
        instance.story.update_status()

@receiver([post_save, post_delete], sender=AcceptanceCriteria)
def update_story_status_from_criteria(sender, instance, **kwargs):
    if instance.story:
        instance.story.update_status()
