from django.contrib import admin
from .models import UserProfile,SessionalApplication, Availibility, SessionalStaffUser , JobListing

# Define admin view for models
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)


class SessionalApplicationAdmin(admin.ModelAdmin):
    list_display = ('sessional_staff', 'UnitName','preferences',)

class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ("casual_id","day_of_the_week","start_time","end_time",)

class SessionalStaffUserAdmin(admin.ModelAdmin):
    list_display = ('week_availability','days_of_week','timing','preferred_unit','preferred_location','preferred_teaching_styles')

class JobListingAdmin(admin.ModelAdmin):
    list_display = ('unit_name','course_description','required_qualification','teaching_materials','session_times','responsibilities','benefits')

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(SessionalApplication, SessionalApplicationAdmin)
admin.site.register(Availibility, AvailabilityAdmin)
admin.site.register(SessionalStaffUser,SessionalStaffUserAdmin)
admin.site.register(JobListing,JobListingAdmin)