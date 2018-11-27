from django.urls import path
from users.views import UserDetailView, UserEditView, UserCreateView, UserListView, UserDeleteView

urlpatterns = [
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('edit/<int:pk>/', UserEditView.as_view(), name='user-edit'),
    path('add/', UserCreateView.as_view(), name='user-create'),
    path('list/', UserListView.as_view(), name='user-list'),
    path('delete/', UserDeleteView.as_view(), name='user-delete')
]


