from django.urls import path
from .views import todoView , deleteView , DoneView , createView
app_name= 'doing'

urlpatterns=[
    path('',todoView.as_view(),name='todo-list'),
    path('delete/<int:pk>/',deleteView.as_view(),name='todo-delete'),
    path('done/<int:pk>/',DoneView.as_view(),name='todo-done'),
    path('create/',createView.as_view(),name='todo-create'),
]