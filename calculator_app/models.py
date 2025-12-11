from django.db import models

# Create your models here.
class Contact(models.Model):
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    email=models.EmailField()
    number=models.CharField(max_length=15)
    message=models.TextField()

    def __str__(self):
        return self.firstName+", "+self.lastName+" ,"+self.email+" ,"+self.number+", "+self.message