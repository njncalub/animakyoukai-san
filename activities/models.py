import os
import datetime

from django.db import models
from django.utils.timezone import utc

from profiling.models import Person

optional = {
    'blank': True,
    'null': True,
}

class Meeting(models.Model):
    name = models.CharField(max_length=200)
    meeting_date = models.DateField('date', **optional)
    description = models.CharField(max_length=200, **optional)
    minutes = models.TextField(max_length=2000, **optional)

    people = models.ManyToManyField(Person, **optional)

    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField(editable=False, **optional)

    def __unicode__(self):
        return u"AMK meeting: {0}".format(self.name)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.today().replace(tzinfo=utc)
        self.modified_at = datetime.datetime.today().replace(tzinfo=utc)

        return super(Meeting, self).save(*args, **kwargs)

    def display_name(self):
        return self.__unicode__()
    display_name.short_description = "Name"

    def people_count(self):
        return len(self.people.all())
    people_count.short_description = "Attendance count"
