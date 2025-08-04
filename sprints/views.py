from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Sprint

# Home view for the AgileIT application

class HomeView(TemplateView):
    template_name = "sprints/homepage.html"

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