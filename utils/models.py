from django.db import models
import uuid


class ModelId(models.Model):
    
    id = models.UUIDField(primary_key=True , default=uuid.uuid4)
    
    class Meta:
        abstract = True