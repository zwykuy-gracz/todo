from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("", views.TodoListView.as_view(), name="todo-list"),
    path("add/", views.TaskCreateView.as_view(), name="add-todo"),
    path("task/<int:pk>/", views.TaskDetailView.as_view(), name="task-details"),
    path("task/<int:pk>/edit/", views.TaskUpdateView.as_view(), name="task-edit"),
    path("task/<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task-delete"),
    path("serializer/", views.TasksList.as_view(), name="dish_list"),
    path("durations/", views.TimeHorizonList.as_view(), name="horizons_list"),
    path("status/", views.StatusList.as_view(), name="horizons_list"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
