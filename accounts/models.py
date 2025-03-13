from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    USER_TYPES = (
        ('customer', 'Customer'),
        ('admin', 'Administrator'),
        ('agent', 'Agent'),
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    
    user_type = models.CharField(_('User Type'), max_length=20, choices=USER_TYPES, default='customer')
    gender = models.CharField(_('Gender'), max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    date_of_birth = models.DateField(_('Date of Birth'), null=True, blank=True)
    nationality = models.CharField(_('Nationality'), max_length=100, null=True, blank=True)
    nationality = models.CharField(_('identification'), max_length=100, null=True, blank=True)
    nationality = models.CharField(_('identification_number'), max_length=100, null=True, blank=True)
    nationality = models.CharField(_('identification_type'), max_length=100, null=True, blank=True)
    phone_number = models.CharField(_('Phone Number'), max_length=20, null=True, blank=True)
    address = models.TextField(_('Address'), null=True, blank=True)
    delivery_address = models.TextField(_('Delivery Address'), null=True, blank=True)
    profile_rank = models.IntegerField(_('Profile Rank'), default=0)
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

class NextOfKin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='next_of_kin')
    name = models.CharField(_('Name'), max_length=100)
    relationship = models.CharField(_('Relationship'), max_length=50)
    phone_number = models.CharField(_('Phone Number'), max_length=20)
    occupation = models.CharField(_('Occupation'), max_length=100, null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.user.username}'s Next of Kin"