# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Customer(models.Model):

    #__Customer_FIELDS__
    idnumber = models.IntegerField(null=True, blank=True)
    fullname = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)

    #__Customer_FIELDS__END

    class Meta:
        verbose_name        = _("Customer")
        verbose_name_plural = _("Customer")


class Users(models.Model):

    #__Users_FIELDS__
    fullname = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    passwordhash = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)
    createdat = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Users_FIELDS__END

    class Meta:
        verbose_name        = _("Users")
        verbose_name_plural = _("Users")


class Suppliers(models.Model):

    #__Suppliers_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    contactperson = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)

    #__Suppliers_FIELDS__END

    class Meta:
        verbose_name        = _("Suppliers")
        verbose_name_plural = _("Suppliers")


class Categories(models.Model):

    #__Categories_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Categories_FIELDS__END

    class Meta:
        verbose_name        = _("Categories")
        verbose_name_plural = _("Categories")


class Products(models.Model):

    #__Products_FIELDS__
    productname = models.CharField(max_length=255, null=True, blank=True)
    categoryid = models.ForeignKey(Categories, on_delete=models.CASCADE)
    supplierid = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    quantityinstock = models.IntegerField(null=True, blank=True)
    reorderlevel = models.IntegerField(null=True, blank=True)
    unitprice = models.CharField(max_length=255, null=True, blank=True)
    createdat = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Products_FIELDS__END

    class Meta:
        verbose_name        = _("Products")
        verbose_name_plural = _("Products")



#__MODELS__END
