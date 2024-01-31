from django.db import models

class Resume(models.Model);
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name