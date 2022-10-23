from django.db import models

class Classes(models.Model):
    class_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')