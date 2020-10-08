import uuid

from django.db import models

# Create your models here.
class Employee(models.Model):
    # employee_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    User_name=models.CharField(max_length=200)
    Password=models.CharField(max_length=50)
    Name=models.CharField(max_length=200)
    Age=models.IntegerField()
    Profile_img=models.ImageField(upload_to='upload/')

    def __str__(self):
        return self.User_name
