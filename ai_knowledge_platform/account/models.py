from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
# Create your models here.

class BaseModel(models.Model):
    id = models.CharField(max_length=36, default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


class CustomeUser(BaseModel, AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(default="")
    profile_image = models.FileField(upload_to="profiles/", blank=True, null=True)

    def __str__(self):
        return self.username
    
