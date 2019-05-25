from django.shortcuts import HttpResponse
from django.core import serializers
from .models import Person, Task
import json

# Create your views here.
def index(request):
    if request.method == 'POST':
        print(request.body)
        formData = json.loads(request.body.decode())
        # create the task using converted formData
        task = Task.objects.create(title=formData['title'], description=formData['description'])
        # get the person we're assigning task to
        assigned_to = Person.objects.get(id=formData['assigned'])
        # make the relationship
        task.assigned.add(assigned_to)
        # serialize the data so we can send back
        data = serializers.serialize("json", [task], use_natural_foreign_keys=True)
    else:  # it's a get request, send back resources
        data = serializers.serialize("json", Task.objects.all(), indent=2, use_natural_foreign_keys=True)
    
    return HttpResponse(data, content_type="application/json", status=200)

def show(request, task_id):
    data = serializers.serialize("json", Task.objects.filter(id=task_id), indent=2, use_natural_foreign_keys=True)
    return HttpResponse(data, content_type="application/json", status=200)

def destroy(request, task_id):
    # get the task
    del_task = Task.objects.get(id=task_id)
    # serialize the task so we can return via httprepsonse
    data = serializers.serialize("json", [del_task], use_natural_foreign_keys=True)
    # clear all many to many relationships
    del_task.assigned.clear()
    # delete the task
    del_task.delete()
    return HttpResponse(data, content_type="application/json", status=200)


def index_people(request):
    data = serializers.serialize("json", Person.objects.all().order_by('first_name'))
    return HttpResponse(data, content_type="application/json", status=200)
