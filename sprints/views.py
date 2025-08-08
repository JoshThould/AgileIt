from multiprocessing import context
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
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Sprint, Story, 

# Dashboard view with Kanban functionality
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'sprints/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stories_todo'] = Story.objects.filter(status='To Do', owner=self.request.user)
        context['stories_in_progress'] = Story.objects.filter(status='In Progress', owner=self.request.user)
        context['stories_done'] = Story.objects.filter(status='Done', owner=self.request.user)
        return context
    
# Kanban board view
class KanbanBoardView(LoginRequiredMixin, TemplateView):
    template_name = 'sprints/kanban.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stories_by_status'] = {
            'To Do': Story.objects.filter(status='To Do', owner=self.request.user),
            'In Progress': Story.objects.filter(status='In Progress', owner=self.request.user),
            'Done': Story.objects.filter(status='Done', owner=self.request.user),
        }
        return context

# Sprints Views
# List all sprints
class SprintListView(LoginRequiredMixin, ListView):
    model = Sprint
    template_name = 'sprints/sprint_list.html'
    context_object_name = 'sprints'

# Create a new sprint
class SprintCreateView(LoginRequiredMixin, CreateView):
    model = Sprint
    fields = ['title', 'start_date', 'end_date']
    template_name = 'sprints/sprint_form.html'
    success_url = reverse_lazy('sprints:sprint-list')

# View sprint details
class SprintDetailView(LoginRequiredMixin, DetailView):
    model = Sprint
    template_name = 'sprints/sprint_detail.html'
    context_object_name = 'sprint'

# Edit an existing sprint
class SprintUpdateView(LoginRequiredMixin, UpdateView):
    model = Sprint
    fields = ['title', 'start_date', 'end_date']
    template_name = 'sprints/sprint_form.html'
    success_url = reverse_lazy('sprints:sprint-list')

# Delete a sprint
class SprintDeleteView(LoginRequiredMixin, DeleteView):
    model = Sprint
    template_name = 'sprints/sprint_confirm_delete.html'
    success_url = reverse_lazy('sprints:sprint-list')

# Story Views
# List all Stories
class StoryListView(LoginRequiredMixin, ListView):
    model = Story
    template_name = 'sprints/story_list.html'
    context_object_name = 'stories'

# Create a new Story
class StoryCreateView(LoginRequiredMixin, CreateView):
    model = Story
    fields = ['title', 'description', 'status']
    template_name = 'sprints/story_form.html'
    success_url = reverse_lazy('sprints:story-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

# View Story details
class StoryDetailView(LoginRequiredMixin, DetailView):
    model = Story
    template_name = 'sprints/story_detail.html'
    context_object_name = 'story'

# Edit an existing Story
class StoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Story
    fields = ['title', 'description', 'status']
    template_name = 'sprints/story_form.html'
    success_url = reverse_lazy('sprints:story-list')

    def test_func(self):
        story = self.get_object()
        return story.owner == self.request.user

# Delete a Story
class StoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Story
    template_name = 'sprints/story_confirm_delete.html'
    success_url = reverse_lazy('sprints:story-list')

    def test_func(self):
        story = self.get_object()
        return story.owner == self.request.user

