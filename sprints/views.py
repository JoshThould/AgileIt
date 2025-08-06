from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Sprint, Epic, Story, AcceptanceCriteria, Task

# Dashboard view for the AgileIT application

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'sprints/dashboard.html'

# List all sprints

class SprintListView(ListView):
    model = Sprint
    template_name = 'sprints/sprint_list.html'
    context_object_name = 'sprints'

# Create a new sprint
class SprintCreateView(CreateView):
    model = Sprint
    fields = ['title', 'start_date', 'end_date']
    template_name = 'sprints/sprint_form.html'
    success_url = reverse_lazy('sprints:sprint-list')

# View sprint details
class SprintDetailView(DetailView):
    model = Sprint
    template_name = 'sprints/sprint_detail.html'
    context_object_name = 'sprint'

# Edit an existing sprint
class SprintUpdateView(UpdateView):
    model = Sprint
    fields = ['title', 'start_date', 'end_date']
    template_name = 'sprints/sprint_form.html'
    success_url = reverse_lazy('sprints:sprint-list')

# Delete a sprint
class SprintDeleteView(DeleteView):
    model = Sprint
    template_name = 'sprints/sprint_confirm_delete.html'
    success_url = reverse_lazy('sprints:sprint-list')

# List all Epics
class EpicListView(ListView):
    model = Epic
    template_name = 'sprints/epic_list.html'
    context_object_name = 'epics'

# Create a new Epic
class EpicCreateView(CreateView):
    model = Epic
    fields = ['title', 'description', 'sprint']
    template_name = 'sprints/epic_form.html'
    success_url = reverse_lazy('sprints:epic-list')

# View Epic details
class EpicDetailView(DetailView):
    model = Epic
    template_name = 'sprints/epic_detail.html'
    context_object_name = 'epic'

# Edit an existing Epic
class EpicUpdateView(UpdateView):
    model = Epic
    fields = ['title', 'description', 'sprint']
    template_name = 'sprints/epic_form.html'
    success_url = reverse_lazy('sprints:epic-list')

# Delete an Epic
class EpicDeleteView(DeleteView):
    model = Epic
    template_name = 'sprints/epic_confirm_delete.html'
    success_url = reverse_lazy('sprints:epic-list')

# List all Stories
class StoryListView(ListView):
    model = Story
    template_name = 'sprints/story_list.html'
    context_object_name = 'stories'

# Create a new Story
class StoryCreateView(CreateView):
    model = Story
    fields = ['title', 'description', 'epic']
    template_name = 'sprints/story_form.html'
    success_url = reverse_lazy('sprints:story-list')

# View Story details
class StoryDetailView(DetailView):
    model = Story
    template_name = 'sprints/story_detail.html'
    context_object_name = 'story'

# Edit an existing Story
class StoryUpdateView(UpdateView):
    model = Story
    fields = ['title', 'description', 'epic']
    template_name = 'sprints/story_form.html'
    success_url = reverse_lazy('sprints:story-list')

# Delete a Story
class StoryDeleteView(DeleteView):
    model = Story
    template_name = 'sprints/story_confirm_delete.html'
    success_url = reverse_lazy('sprints:story-list')

# List all Acceptance Criteria
class AcceptanceCriteriaListView(ListView):
    model = AcceptanceCriteria
    template_name = 'sprints/acceptance_criteria_list.html'
    context_object_name = 'acceptance_criteria'

# Create a new Acceptance Criteria
class AcceptanceCriteriaCreateView(CreateView):
    model = AcceptanceCriteria
    fields = ['title', 'description', 'story']
    template_name = 'sprints/acceptance_criteria_form.html'
    success_url = reverse_lazy('sprints:acceptance-criteria-list')

# View Acceptance Criteria details
class AcceptanceCriteriaDetailView(DetailView):
    model = AcceptanceCriteria
    template_name = 'sprints/acceptance_criteria_detail.html'
    context_object_name = 'acceptance_criteria'

# Edit an existing Acceptance Criteria
class AcceptanceCriteriaUpdateView(UpdateView):
    model = AcceptanceCriteria
    fields = ['title', 'description', 'story']
    template_name = 'sprints/acceptance_criteria_form.html'
    success_url = reverse_lazy('sprints:acceptance-criteria-list')

# Delete an Acceptance Criteria
class AcceptanceCriteriaDeleteView(DeleteView):
    model = AcceptanceCriteria
    template_name = 'sprints/acceptance_criteria_confirm_delete.html'
    success_url = reverse_lazy('sprints:acceptance-criteria-list')

# List all Tasks
class TaskListView(ListView):
    model = Task
    template_name = 'sprints/task_list.html'
    context_object_name = 'tasks'

# Create a new Task
class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'story']
    template_name = 'sprints/task_form.html'
    success_url = reverse_lazy('sprints:task-list')

# View Task details
class TaskDetailView(DetailView):
    model = Task
    template_name = 'sprints/task_detail.html'
    context_object_name = 'task'

# Edit an existing Task
class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'story']
    template_name = 'sprints/task_form.html'
    success_url = reverse_lazy('sprints:task-list')

# Delete a Task
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'sprints/task_confirm_delete.html'
    success_url = reverse_lazy('sprints:task-list')
