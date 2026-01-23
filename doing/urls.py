from django.urls import path
from .views import todoView , deleteView , updateView , createView
app_name= 'doing'

urlpatterns=[
    path('',todoView.as_view(),name='todo-list'),
    path('delete/<int:pk>/',deleteView.as_view(),name='todo-delete'),
    path('update/<int:pk>/',updateView.as_view(),name='todo-update'),
    path('create/',createView.as_view(),name='todo-create')
]