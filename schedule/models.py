from django.db import models

# Create your models here.
class Show(models.Model):
    title= models.CharField(max_length=255)
    network= models.CharField(max_length=255)
    release_date= models.DateField()
    desc= models.TextField(null=True)
    created_time= models.DateTimeField(auto_now_add=True)
    updated_time= models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"{self.title} ({self.id})"