from django.db import models
from datetime import date,datetime
from django.utils import timezone
from django.utils.timezone import activate
from django.utils.timezone import get_current_timezone
# from trainings.models import Training
# from django.forms import ModelForm, TextArea
# Create your models here.

priority_choices = (
    ('High','High'),('Moderate','Moderate'),('Low','Low'))
class TodoList(models.Model):
    task = models.CharField(max_length=300,null=True, blank=True)
    task_image = models.ImageField(null=True, blank=True, upload_to="images/")
    priority = models.CharField(max_length=10,choices=priority_choices,default="Moderate")
    deadline = models.DateField()
    def display(self):
        return self.task+" "+self.task_image

    
    @property
    def is_past_due(self):
        # self.deadline = utc.localize(self.deadline)
        # new_deadline = self.deadline.replace(tzinfo=utc)
        if date.today() > self.deadline:
            print("Timezone" ,timezone.now())
            return True
        return False
    # def save(self):
    #     task = self.c
    #     super(Blog, self).save(*args, **kwargs) # Call the "real" save() method.
    #     do_something_else()



