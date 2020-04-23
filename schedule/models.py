from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def basic_validator(self,postData):   
        print("*"*100)
        print('VALIDATOR IS HERE!!!')
        print(postData['title'])
        errors = {}
        if len(postData['title']) == 0:
            errors['title']="Title can not be empty"
        elif len(postData['title'])<2:
            errors['title']="Title can not be less than 2 characters"

        if len(postData['network'])==0:
            errors['network']="Network can not be empty"
        elif len(postData['network'])<3:
            errors['network']="Network can not be less than 3 characters"

        if len(postData['release_date'])==0:
            errors['release_date']="Release date can not be empty"
        
        if len(postData['desc'])==0:
            errors['desc']="Description can not be empty"
        elif len(postData['desc'])<10:
            errors['desc']="Description is too short! Please type more information!"
        return errors
        
    def basic_validator_bonus(self,postData):
        errors={}
        if len(postData['title'])==0:
            errors['title']="Title can not be empty"
        elif len(postData['title'])<2:
            errors['title']="Title can not be less than 2 characters"

        if len(postData['network'])==0:
            errors['network']="Network can not be empty"
        elif len(postData['network'])<3:
            errors['network']="Network can not be less than 3 characters"
        now=datetime.now().strftime('%Y-%m-%d')
        print (now)
        if len(postData['release_date'])==0:
            errors['release_date']="Release date can not be empty"
        elif postData['release_date']>now:
            errors['release_date']="you have to choose aired show"
        
        if len(postData['desc'])>0 and len(postData['desc'])<10:
            errors['desc']="Description is too short! Please type more information or leave it empty!"
        return errors
# Create your models here.
class Show(models.Model):
    title= models.CharField(max_length=255)
    network= models.CharField(max_length=255)
    release_date= models.DateField()
    desc= models.TextField(null=True)
    created_time= models.DateTimeField(auto_now_add=True)
    updated_time= models.DateTimeField(auto_now=True)
    objects= ShowManager()

    def __repr__(self):
        return f"{self.title} ({self.id})"
    