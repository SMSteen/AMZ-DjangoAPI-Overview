from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __repr__(self):
        return f'{self.id} {self.first_name} {self.last_name}'

    def natural_key(self):
        return( {'id': self.id, 'first_name': self.first_name, 'last_name': self.last_name} )

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(default='')
    assigned = models.ManyToManyField(Person, related_name="tasks")
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'{self.id} {self.title}'