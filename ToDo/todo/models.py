from django.db import models
from django.forms import ModelForm


# Create your models here.
class ListEntry(models.Model):
    Id = models.AutoField(primary_key=True)
    Description = models.CharField(max_length=200)
    isDone = models.BooleanField()
    class Meta:
        db_table: "listentry"
