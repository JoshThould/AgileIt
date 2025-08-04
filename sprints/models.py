from django.db import models
from django.contrib.auth.models import User


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

    def __str__(self):
        return f"Sprint: {self.title} ({self.start_date} to {self.end_date})"



class Epic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    sprint = models.ForeignKey(Sprint, related_name='epics', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} – Epic in Sprint '{self.sprint.title}'"



class Story(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TODO')
    epic = models.ForeignKey(Epic, related_name='stories', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} [{self.status}] in Epic '{self.epic.title}'"



    # TODO: Add update_status logic to Story model and signals from Task & Criteria after initial setup


class AcceptanceCriteria(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TODO')
    story = models.ForeignKey(Story, related_name='acceptance_criteria', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} [{self.status}] in Story '{self.story.title}'"



class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TODO')
    story = models.ForeignKey(Story, related_name='tasks', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} [{self.status}] in Story '{self.story.title}'"
    
# Update Status Logic:
# Automatically updates Story status based on completion of related Tasks and Acceptance Criteria.
# Sets status to "Done" only if all Tasks are marked complete and all Criteria are met.

class Story(models.Model):
    STATUS_CHOICES = [
        ("To Do", "To Do"),
        ("In Progress", "In Progress"),
        ("Done", "Done"),
    ]
    title = models.CharField(max_length=200)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, related_name="stories")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="To Do")
    # other fields...

    def update_status(self):
        all_tasks_done = self.tasks.filter(status__in=["To Do", "In Progress"]).count() == 0
        all_criteria_met = self.criteria.filter(is_met=False).count() == 0

        if all_tasks_done and all_criteria_met:
            self.status = "Done"
        else:
            # Optional: downgrade status if needed
            if self.tasks.filter(status="In Progress").exists():
                self.status = "In Progress"
            else:
                self.status = "To Do"
        self.save()
