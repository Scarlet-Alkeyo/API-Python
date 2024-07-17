from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email= models.EmailField()
    phone_number =models.CharField(max_length=20)
    department= models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    gender= models.CharField(max_length=20)
    bio =models.CharField(max_length=20)
    staff_id =models.CharField(max_length=20)





    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"