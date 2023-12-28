from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from core_user.serializers import UserInfoSerializer
from core.models import Label , Task



class LabelSerializer(ModelSerializer):
    name = serializers.CharField(source='title')
    class Meta:
        model = Label
        fields = [
            'id',
            'name',
            'slug',
            'description',
        ]
        
class LabelPostSerializer(ModelSerializer):
    
    name = serializers.CharField(source='title')
    
    class Meta:
        model = Label
        fields = [
            'name',
            'description'
        ]
    
    def create(self, validated_data):
        
        # name = validated_data.get('title')
        # description = validated_data.get('description')
        
        # print(name)
        # print(description)
        return super().create(validated_data)
        
        
class LabelDetailSerializer(ModelSerializer):
    
    class Meta:
        model = Label
        fields = '__all__'
        

class TaskLabelInfoSerializer(ModelSerializer):
    name = serializers.CharField(source='title')
    class Meta:
        model = Label
        fields = [
            'id',
            'name',
        ]

class TaskSerializer(ModelSerializer):
    
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(source='title')
    label = TaskLabelInfoSerializer(many=False)
    user = UserInfoSerializer(many=False)
    
    class Meta:
        model = Task
        fields = [
            'id',
            'name',
            'slug',
            'description',
            'label',
            'user'
        ]
        
class TaskPostSerializer(ModelSerializer):
    
    name = serializers.CharField(source='title')
    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'label',
        ]
        
    
    def create(self, validated_data):
        
        title = validated_data.get('title')
        description = validated_data.get('description')
        label = validated_data.get('label')
        
        return Task.objects.create(title=title, description=description, label=label , user_id=self.context['user_id'])