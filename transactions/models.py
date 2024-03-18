from django.db import models
from django.utils import timezone



# Create your models here.
class Transaction(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    type = models.CharField(max_length=7)
    title = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    periodicity = models.CharField(max_length=7)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey('users.User', related_name='transactions', on_delete=models.CASCADE)

    def __str__(self):
        return self.title