from django.contrib import admin
from .models import UserProfile, PermanentStaff, SessionalStaff, SessionalApplication, Availibility, SessionalStaffUser , JobListing

# Define admin view for models
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

class PermanentStaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'qualifications', 'availability')

class SessionalStaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'qualifications', 'availability')

# class UnitAdmin(admin.ModelAdmin):
#     list_display = ('UnitName',)

class SessionalApplicationAdmin(admin.ModelAdmin):
    list_display = ('sessional_staff', 'unit', 'preferences')

class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ("casual_id","day_of_the_week","start_time","end_time",)

class SessionalStaffUserAdmin(admin.ModelAdmin):
    list_display = ('email','password','phoneno','dob','gender','education','certification','work_experience',
        'week_availability','days_of_week','timing','preferred_unit','preferred_location','preferred_teaching_styles')

class JobListingAdmin(admin.ModelAdmin):
    list_display = ('sessional_staff','first_name','unit','num_applications','roles',)

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(PermanentStaff, PermanentStaffAdmin)
admin.site.register(SessionalStaff,SessionalStaffAdmin)
admin.site.register(SessionalApplication, SessionalApplicationAdmin)
# admin.site.register(Unit, UnitAdmin)
admin.site.register(Availibility, AvailabilityAdmin)
admin.site.register(SessionalStaffUser,SessionalStaffUserAdmin)
admin.site.register(JobListing,JobListingAdmin)