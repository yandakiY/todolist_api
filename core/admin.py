from django.contrib import admin
from core.models import Label , Task , Notification

# Register your models here.

@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'slug' , 'description' , 'created']
    # pass
    
    
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'slug' , 'description' , 'created' , 'time_reminder' , 'label' , 'user']
    
    
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id' , 'user' , 'task']