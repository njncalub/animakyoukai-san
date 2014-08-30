import os
import datetime
from uuid import uuid4

from django.db import models≈

from member_profiling.constants import (
    SEX_CHOICES,
    CIVIL_STATUS_CHOICES,
    EDUCATIONAL_ATTAINMENT_CHOICES,
    MEMBER_STATUS_CHOICES
)

optional = {
    'blank': True,
    'null': True,
}

class Person(models.Model):

    def get_upload_path(instance, filename):
        fname, dot, extension = filename.rpartition('.')
        new_name = '%s.%s' % (str(uuid4().hex), extension)
        return os.path.join("images", "avatars", new_name)

    avatar = models.ImageField("Profile Avatar", upload_to=get_upload_path, **optional)
    last_name = models.CharField(max_length=200, **optional)
    first_name = models.CharField(max_length=200, **optional)
    middle_name = models.CharField(max_length=200, **optional)
    nick_name = models.CharField(max_length=200, **optional)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, **optional)
    birth_date = models.DateTimeField('birth date', **optional)
    address = models.TextField(max_length, **optional)
    mobile_number = models.CharField(max_length=200, **optional)
    landline_number = models.CharField(max_length=200, **optional)
    email_address = models.EmailField(max_length=200, **optional)
    website_address = models.URLField(max_length=200, **optional)
    application_date = models.DateTimeField('date of application', **optional)
    member_status = models.CharField(max_length=12, choices=MEMBER_STATUS_CHOICES, **optional)
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField(**optional)

    def __unicode__(self):
        return u"{0}, {1}".format(self.last_name, self.first_name)

    def save(self, *args, *kwargs):
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.modified_at = datetime.datetime.today()

        return super(Person, self).save(*args, *kwargs)

    def calculate_age(self):
        today = datetime.date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))

