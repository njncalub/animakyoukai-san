from django.contrib import admin
from activities.models import Meeting

class MeetingAdmin(admin.ModelAdmin):
    model = Meeting
    list_display = ('display_name', 'meeting_date', 'location', 'description', 'people_count',)
    list_filter = ('meeting_date',)
    filter_horizontal = ('people',)
    search_fields = ('name', 'location', 'description', 'minutes',)

admin.site.register(Meeting, MeetingAdmin)
