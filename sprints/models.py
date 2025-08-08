from django.db import models
from django.contrib.auth.models import User

# Status Choices
STATUS_CHOICES = [
    ("To Do", "To Do"),
    ("In Progress", "In Progress"),
    ("Done", "Done"),
]

# Sprint Model
class Sprint(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Sprint: {self.title} ({self.start_date} to {self.end_date})"

# Story Model
class Story(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="To Do")
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, null=True, blank=True, related_name="stories")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} [{self.status}]"

    def update_status(self):
        all_tasks_done = self.tasks.filter(status__in=["To Do", "In Progress"]).count() == 0
        all_criteria_met = self.acceptance_criteria.filter(status__in=["To Do", "In Progress"]).count() == 0

        if all_tasks_done and all_criteria_met:
            self.status = "Done"
        elif self.tasks.filter(status="In Progress").exists() or self.acceptance_criteria.filter(status="In Progress").exists():
            self.status = "In Progress"
        else:
            self.status = "To Do"
        self.save()


# Acceptance Criteria Model
class AcceptanceCriteria(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="To Do")
    story = models.ForeignKey(Story, related_name='acceptance_criteria', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} [{self.status}] in Story '{self.story.title}'"

# Task Model
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="To Do")
    story = models.ForeignKey(Story, related_name='tasks', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} [{self.status}] in Story '{self.story.title}'"