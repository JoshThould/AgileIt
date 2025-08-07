app_name = "sprints"

from django.urls import path
from .views import DashboardView
from . import views


urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),  # Root dashboard view
    path('sprints/', views.SprintListView.as_view(), name='sprint-list'),
    path('sprints/create/', views.SprintCreateView.as_view(), name='sprint-create'),
    path('epics/', views.EpicListView.as_view(), name='epic-list'),
    path('epics/create/', views.EpicCreateView.as_view(), name='epic-create'),
    path('stories/', views.StoryListView.as_view(), name='story-list'),
    path('stories/create/', views.StoryCreateView.as_view(), name='story-create'),
    path('acceptancecriteria/', views.AcceptanceCriteriaListView.as_view(), name='acceptance-criteria-list'),
    path('acceptancecriteria/create/', views.AcceptanceCriteriaCreateView.as_view(), name='acceptance-criteria-create'),
    path('tasks/', views.TaskListView.as_view(), name='task-list'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task-create'),
    path('sprints/<int:pk>/', views.SprintDetailView.as_view(), name='sprint-detail'),
    path('sprints/<int:pk>/edit/', views.SprintUpdateView.as_view(), name='sprint-edit'),
    path('sprints/<int:pk>/delete/', views.SprintDeleteView.as_view(), name='sprint-delete'),
    path('epics/<int:pk>/', views.EpicDetailView.as_view(), name='epic-detail'),
    path('epics/<int:pk>/edit/', views.EpicUpdateView.as_view(), name='epic-edit'),
    path('epics/<int:pk>/delete/', views.EpicDeleteView.as_view(), name='epic-delete'),
    path('stories/<int:pk>/', views.StoryDetailView.as_view(), name='story-detail'),
    path('stories/<int:pk>/edit/', views.StoryUpdateView.as_view(), name='story-edit'),
    path('stories/<int:pk>/delete/', views.StoryDeleteView.as_view(), name='story-delete'),
    path('acceptancecriteria/<int:pk>/', views.AcceptanceCriteriaDetailView.as_view(), name='acceptance-criteria-detail'),
    path('acceptancecriteria/<int:pk>/edit/', views.AcceptanceCriteriaUpdateView.as_view(), name='acceptance-criteria-edit'),
    path('acceptancecriteria/<int:pk>/delete/', views.AcceptanceCriteriaDeleteView.as_view(), name='acceptance-criteria-delete'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task-edit'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),
]