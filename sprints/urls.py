app_name = "sprints"

from django.urls import path
from .views import (
    DashboardView,
    SprintKanbanView,
    SprintListView,
    SprintCreateView,
    SprintDetailView,
    SprintUpdateView,
    SprintDeleteView,
    StoryListView,
    StoryCreateView,
    StoryDetailView,
    StoryUpdateView,
    StoryDeleteView,
)

urlpatterns = [
    # Dashboard
    path('', DashboardView.as_view(), name='dashboard'),


    # Sprints
    path('list/', SprintListView.as_view(), name='sprint-list'),
    path('sprints/new/', SprintCreateView.as_view(), name='sprint-create'),
    path('sprints/<int:pk>/', SprintDetailView.as_view(), name='sprint-detail'),
    path('sprints/<int:pk>/edit/', SprintUpdateView.as_view(), name='sprint-edit'),
    path('sprints/<int:pk>/delete/', SprintDeleteView.as_view(), name='sprint-delete'),
    path('sprints/<int:pk>/kanban/', SprintKanbanView.as_view(), name='sprint-kanban'),

    # Stories
    path('stories/', StoryListView.as_view(), name='story-list'),
    path('stories/new/', StoryCreateView.as_view(), name='story-create'),
    path('stories/<int:pk>/', StoryDetailView.as_view(), name='story-detail'),
    path('stories/<int:pk>/edit/', StoryUpdateView.as_view(), name='story-edit'),
    path('stories/<int:pk>/delete/', StoryDeleteView.as_view(), name='story-delete'),
]