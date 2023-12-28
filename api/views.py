from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet , GenericViewSet
from rest_framework.mixins import CreateModelMixin , DestroyModelMixin , RetrieveModelMixin
from core.models import Label , Task
from .serializers import LabelPostSerializer , TaskUpdateSerializer , LabelSerializer , LabelDetailSerializer , TaskSerializer , TaskPostSerializer

# Create your views here.

class LabelViewSet(ModelViewSet):
    queryset = Label.objects.all()
    
    def get_serializer_class(self):
        
        if self.action == 'retrieve':
            return LabelDetailSerializer
        
        if self.request.method == 'POST':
            return LabelPostSerializer
        return LabelSerializer
    
    
class TaskViewSet(ModelViewSet):
    
    queryset = Task.objects.all()
    
    def get_queryset(self):
        return Task.objects.filter(user_id=self.request.user.id)
    
    def get_serializer_context(self):
        return {'user_id':self.request.user.id}
    
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TaskPostSerializer
        
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return TaskUpdateSerializer
        return TaskSerializer