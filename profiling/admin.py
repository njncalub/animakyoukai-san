from django.contrib import admin
from profiling.models import Person

class PersonAdmin(admin.ModelAdmin):
    model = Person
    list_display = ('image_tag', 'last_name', 'first_name', 'nick_name', 'sex', 'birth_date', 'mobile_number', 'member_status')
    list_filter = ('sex', 'application_date', 'member_status')
    search_fields = ['last_name', 'first_name', 'middle_name', 'nick_name', 'mobile_number', 'landline_number', 'address']

admin.site.register(Person, PersonAdmin)
