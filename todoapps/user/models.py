import os
import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from todoapps.common.models import BaseModel, File
from todoapps.user.manager import UserManager


def get_profile_picture_upload_path(_, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('user/profile-pictures/', filename)


def get_cover_image_upload_path(_, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('user/cover-image/', filename)


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(unique=True, max_length=20)
    email = models.EmailField(max_length=45, unique=True, error_messages={
        'unique': "A user with that email already exists.",
    }, )
    first_name = models.CharField(max_length=45)
    middle_name = models.CharField(max_length=45, null=True, blank=True)
    last_name = models.CharField(max_length=45)
    profile_picture = models.ForeignKey(
        File, related_name='user_profile', null=True, blank=True, on_delete=models.CASCADE)
    cover_image = models.ForeignKey(
        File, related_name='user_cover', null=True, blank=True, on_delete=models.CASCADE)
    last_login = models.DateTimeField('last login', blank=True, null=True)
    last_activity = models.DateTimeField(
        'last activity', blank=True, null=True)
    contact_number = models.CharField(max_length=14, null=True, blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    ACCOUNT_REGISTRATION_FIELDS = [
        'email', 'first_name', 'last_name', 'password', 'contact_number']

    _send_password_change_email = False
    add_this_password_to_history = None

    # pylint: disable=W0201
    def set_password(self, raw_password):
        super().set_password(raw_password)
        self.add_this_password_to_history = self.password

    @property
    def profile_picture_thumb(self):
        if self.profile_picture:
            return self.profile_picture.file

        from django.templatetags.static import static
        return static('user/images/default.png')

    @property
    def is_staff(self):
        return self.is_superuser

    @property
    def display_name(self):
        return f"{self.first_name} {self.last_name}".title() if not self.middle_name \
            else f"{self.first_name} {self.middle_name} {self.last_name}".title()

    def __str__(self):
        return f"{self.email}"

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        instance = super().save(*args, **kwargs)
        return instance
