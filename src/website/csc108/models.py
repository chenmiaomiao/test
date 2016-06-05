# _*_ coding: utf8 _*_

from __future__ import unicode_literals

from django.db import models

class new_account(models.Model):
    id_front = models.ImageField()
    id_back = models.ImageField()
    id_number = models.CharField(max_length = 18)
    phone_number = models.CharField(max_length = 11)
    password = models.CharField(max_length = 6)
    verification_code = models.CharField(max_length = 4)