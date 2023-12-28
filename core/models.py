from django.db import models
from utils.models import ModelId
from django_extensions.db.models import TitleSlugDescriptionModel , ActivatorModel, TimeStampedModel
from todolist_api import settings


class Label(TitleSlugDescriptionModel, ActivatorModel , TimeStampedModel):
    
    def __str__(self):
        return f'{self.title}'
    

class Task(TitleSlugDescriptionModel , ActivatorModel , TimeStampedModel , ModelId):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.PROTECT)
    label = models.ForeignKey(Label , on_delete=models.CASCADE , related_name='items')
    time_reminder = models.DateTimeField(blank=True, null=True, help_text=('Time reminder for create a notification') , default=None)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ['-created']

    def __str__(self):
        return f'{self.title}'
    
class Notification(ModelId , TimeStampedModel):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.PROTECT)
    task = models.ForeignKey(Task , on_delete=models.PROTECT)
    # created_notif = models.DateTimeField(blank=True, null=True)
    