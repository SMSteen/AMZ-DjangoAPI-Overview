from django.urls import path
from . import views


urlpatterns = [
    path('tasks/', views.index),  # gets list of all tasks OR posts new tasks
    path('tasks/<int:task_id>', views.show),  # gets one task
    path('tasks/<int:task_id>/delete', views.destroy),  # deteles one task
    path('people/', views.index_people),  # get list of all people
    path('people/<int:person_id>', views.show_person),  # gets one person
]