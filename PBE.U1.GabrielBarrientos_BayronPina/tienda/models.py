from django.db import models


# Create your models here.


phone_codes =(
    ('+56', '+56'),
    ('+54', '+54')
)
class Contact(models.Model):
    first_name = models.CharField(max_length=25,default='')
    second_name = models.CharField(max_length=25, default='')
    first_last_name = models.CharField(max_length=25, default='')
    second_last_name = models.CharField(max_length=25, default='')
    email_adress = models.EmailField(max_length=30, default='')
    number_prefix = models.CharField(max_length=3, choices=phone_codes, default='')
    phone_number  = models.CharField(max_length=9, default='')
    comment = models.TextField(max_length=500, default='')

    def __str__(self):
        return self.first_name


