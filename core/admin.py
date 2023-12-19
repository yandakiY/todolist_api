from django.contrib import admin
from core.models import Label , Task

# Register your models here.

@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'slug' , 'description' , 'created']
    # pass
    
    
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'slug' , 'description' , 'created' , 'label' , 'user']