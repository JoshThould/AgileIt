from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Sprint

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Epic



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

# 🗂 List all Epics
class EpicListView(ListView):
    model = Epic
    template_name = 'sprints/epic_list.html'
    context_object_name = 'epics'

# ➕ Create a new Epic
class EpicCreateView(CreateView):
    model = Epic
    fields = ['title', 'description', 'sprint']
    template_name = 'sprints/epic_form.html'
    success_url = reverse_lazy('sprints:epic-list')

# 🔍 View Epic details
class EpicDetailView(DetailView):
    model = Epic
    template_name = 'sprints/epic_detail.html'
    context_object_name = 'epic'

# ✏️ Edit an existing Epic
class EpicUpdateView(UpdateView):
    model = Epic
    fields = ['title', 'description', 'sprint']
    template_name = 'sprints/epic_form.html'
    success_url = reverse_lazy('sprints:epic-list')

# ❌ Delete an Epic
class EpicDeleteView(DeleteView):
    model = Epic
    template_name = 'sprints/epic_confirm_delete.html'
    success_url = reverse_lazy('sprints:epic-list')

# 🗂 List all Stories
class StoryListView(ListView):
    model = Story
    template_name = 'sprints/story_list.html'
    context_object_name = 'stories'

# ➕ Create a new Story
class StoryCreateView(CreateView):
    model = Story
    fields = ['title', 'description', 'epic']
    template_name = 'sprints/story_form.html'
    success_url = reverse_lazy('sprints:story-list')

# 🔍 View Story details
class StoryDetailView(DetailView):
    model = Story
    template_name = 'sprints/story_detail.html'
    context_object_name = 'story'

# ✏️ Edit an existing Story
class StoryUpdateView(UpdateView):
    model = Story
    fields = ['title', 'description', 'epic']
    template_name = 'sprints/story_form.html'
    success_url = reverse_lazy('sprints:story-list')

# ❌ Delete a Story
class StoryDeleteView(DeleteView):
    model = Story
    template_name = 'sprints/story_confirm_delete.html'
    success_url = reverse_lazy('sprints:story-list')