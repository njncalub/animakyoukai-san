from django.contrib import admin
from profiling.models import Person

class PersonAdmin(admin.ModelAdmin):
    model = Person
    list_display = ('image_tag', 'last_name', 'first_name', 'nick_name', 'sex', 'birth_date', 'mobile_number', 'member_status')

admin.site.register(Person, PersonAdmin)
