from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from users.models import CustomUser


class UserDetailView(DetailView):
    """
    User detatil view
    """
    model = CustomUser


class UserEditView(UpdateView):
    """
    User edit view
    """
    model = CustomUser


class UserCreateView(CreateView):
    """
    User create view
    """
    model = CustomUser
    fields = ['birthday', 'random_number']


class UserListView(ListView):
    """
    User list view
    """
    model = CustomUser


class UserDeleteView(DeleteView):
    """
    User delete view
    """
    model = CustomUser
