from django.urls import path

from .views import TodoView,TododetailView,TodoDeleteView,TodoCreateView,TodoUpdateView

urlpatterns = [
    path('list/', TodoView.as_view(), name='list'),
    path('detail/<int:pk>/', TododetailView.as_view(), name='detail'),
    path('create/', TodoCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', TodoUpdateView.as_view(), name='update'),
]