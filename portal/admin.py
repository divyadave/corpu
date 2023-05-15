from django.contrib import admin
from .models import UserProfile, PermanentStaff, SessionalStaff, Unit, SessionalApplication, Availibility

# Define admin view for models
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

class PermanentStaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'qualifications', 'availability')

class SessionalStaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'qualifications', 'availability')

class UnitAdmin(admin.ModelAdmin):
    list_display = ('name',)

class SessionalApplicationAdmin(admin.ModelAdmin):
    list_display = ('sessional_staff', 'unit', 'preferences')

class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ("casual_id","day_of_the_week","start_time","end_time",)

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(PermanentStaff, PermanentStaffAdmin)
admin.site.register(SessionalStaff,SessionalStaffAdmin)
admin.site.register(SessionalApplication, SessionalApplicationAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Availibility, AvailabilityAdmin)