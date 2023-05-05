from django.urls import path
from . import views

urlpatterns = [
    path('', views.Pr31View.as_view(), name="pr31"),
    path('asd', views.Pr31.as_view(), name="pr31_2"),
    path('todo/', views.TodoItemList.as_view(), name='todo_list'),
    path('todohtml/', views.TodoItemListHTML.as_view(), name='todo_list_html'),
]
