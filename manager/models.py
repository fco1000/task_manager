from django.db import models

# Create your models here.
class Task(models.Model):
    class Level(models.TextChoices):
        High = "High","high"
        Medium = "Medium","medium"
        Low = "Low","low"
        
    task_id = models.CharField(max_length=20)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    assigned_worker = models.ForeignKey('Worker', on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True)
    due_date = models.DateField(null=True, blank=True)
    priority_level  = models.CharField(max_length=10, choices=Level.choices,default=Level.Low)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.title} - {self.priority_level}'
    
    def save(self,*args,**kwargs):
        if not self.task_id:
            last_id = Task.objects.all().count() + 1
            self.task_id = f'T{last_id:03d}'
        super().save(*args, **kwargs)
        
class Worker(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    assigned_tasks = models.ManyToManyField(Task, blank=True)
    
    def __str__(self):
        return self.name