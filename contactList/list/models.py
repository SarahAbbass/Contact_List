import datetime
from django.db import models


class Contact(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=20)
    profession1 = models.CharField(max_length=30)
    profession2 = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    tel_number = models.CharField(max_length=20)
    date_added = models.DateField(default=datetime.date.today())
    objects = models.Manager()

    error_message = models.CharField(max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.profession1 != self.profession2:
            difference_count = sum(1 for a, b in zip(self.profession1, self.profession2) if a != b)
            if difference_count > 1:
                self.error_message = "The content of profession1 and profession2 differs by more than one character."
                return
        super(Contact, self).save(*args, **kwargs)




