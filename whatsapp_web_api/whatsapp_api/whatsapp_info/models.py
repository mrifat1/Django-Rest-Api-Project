from django.db import models

# Create your models here.
class WhatsappInfo(models.Model):
    name = models.CharField(max_length=200,null=False,blank=False)
    phone_number = models.BigIntegerField(primary_key=True)

    def __str__(self):
        return self.name