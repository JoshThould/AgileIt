from django.db import models

# Status Choices

STATUS_CHOICES = [
    ('TODO', 'To Do'),
    ('IN_PROGRESS', 'In Progress'),
    ('DONE', 'Done'),
]


# Create your models here.
class Sprint(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

class Epic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    sprint = models.ForeignKey(Sprint, related_name='epics', on_delete=models.CASCADE)

class Story(models.Model):
    title = models.Charfield(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TODO')
    epic = models.ForeignKey(Epic, related_name='stories', on_delete=models.CASCADE)

    # TODO: Add update_status logic to Story model and signals from Task & Criteria after initial setup


class AcceptanceCriteria(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TODO')
    story = models.ForeignKey(Story, related_name='acceptance_criteria', on_delete=models.CASCADE)

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TODO')
    story = models.ForeignKey(Story, related_name='tasks', on_delete=models.CASCADE)