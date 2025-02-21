from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from rest_framework import generics
from .models import Task, TimeHorizon, TaskStatus
from .serializers import TaskSerializer, DurationSerializer, StatusSerializer

from .forms import TaskForm, UserSignUpForm


class SignUpView(CreateView):
    form_class = UserSignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("todo-list")


@method_decorator([login_required], name="dispatch")
class TodoListView(ListView):
    model = Task
    ordering = ("deadline",)
    context_object_name = "todo_list"
    template_name = "todo-list.html"

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


@method_decorator([login_required], name="dispatch")
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "add-todo.html"
    success_url = "todo-list"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        task = form.save(commit=False)
        task.owner = self.request.user
        task.save()
        return redirect("todo-list")


@method_decorator([login_required], name="dispatch")
class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "task-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@method_decorator([login_required], name="dispatch")
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "edit-task.html"

    def get_success_url(self):
        return reverse("todo-list")


@method_decorator([login_required], name="dispatch")
class TaskDeleteView(DeleteView):
    model = Task

    def get_success_url(self):
        return reverse("todo-list")


@login_required
def post_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.owner == request.user:
        task.delete()
        return redirect("todo-list")
    else:
        return redirect("todo-list")


class TasksList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TimeHorizonList(generics.ListCreateAPIView):
    queryset = TimeHorizon.objects.all()
    serializer_class = DurationSerializer


class StatusList(generics.ListCreateAPIView):
    queryset = TaskStatus.objects.all()
    serializer_class = StatusSerializer
