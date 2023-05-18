from django.db import models
# Create your models here.

class MyModel(models.Model):
    # ...
    imagen = models.ImageField(upload_to='media/')
    from django.db import models
