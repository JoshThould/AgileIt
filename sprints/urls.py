app_name = "sprints"

from django.urls import path
from .views import DashboardView
from .views import KanbanBoardView
from . import views


urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),  # Root dashboard view
    path('kanban/', KanbanBoardView.as_view(), name='kanban-board'),  # Kanban board view
    path('sprints/', views.SprintListView.as_view(), name='sprint-list'),
    path('sprints/create/', views.SprintCreateView.as_view(), name='sprint-create'),
    path('stories/', views.StoryListView.as_view(), name='story-list'),
    path('stories/create/', views.StoryCreateView.as_view(), name='story-create'),
    path('sprints/<int:pk>/', views.SprintDetailView.as_view(), name='sprint-detail'),
    path('sprints/<int:pk>/edit/', views.SprintUpdateView.as_view(), name='sprint-edit'),
    path('sprints/<int:pk>/delete/', views.SprintDeleteView.as_view(), name='sprint-delete'),
    path('stories/<int:pk>/', views.StoryDetailView.as_view(), name='story-detail'),
    path('stories/<int:pk>/edit/', views.StoryUpdateView.as_view(), name='story-edit'),
    path('stories/<int:pk>/delete/', views.StoryDeleteView.as_view(), name='story-delete'),
]