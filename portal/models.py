from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields for the user's profile

    def __str__(self):
        return self.user.username
    

class Staff(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField( max_length=255, unique=True)
    qualifications = models.TextField()
    availability = models.TextField()
    phoneno = models.CharField(max_length=10)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    certification = models.CharField(max_length=255)
    work_experience = models.TextField()

    class Meta:
        abstract = True


class SessionalStaffUser(Staff):
    week_availability = models.CharField(max_length=255)
    days_of_week = models.CharField(max_length=255)
    timing = models.TimeField()
    preferred_unit = models.CharField(max_length=255)
    preferred_location = models.CharField(max_length=255)
    preferred_teaching_styles = models.CharField(max_length=255)


class SessionalApplication(models.Model):
    sessional_staff = models.ForeignKey(SessionalStaffUser, on_delete=models.CASCADE)
    UnitName = models.CharField(max_length=255)
    preferences = models.TextField()

# class Availibility(models.Model):
#     casual_id = models.ForeignKey(SessionalStaffUser, on_delete=models.CASCADE)
   
#     id = models.AutoField(primary_key=True, default=999)

# class JobListing(models.Model):
#     sessional_staff = models.ForeignKey(SessionalStaffUser, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=255, null=True, blank=True)
#     UnitName = models.CharField(max_length=255)
#     num_applications = models.CharField(max_length=255)
#     roles = models.CharField(max_length=255)

#     def __str__(self):
#         return self.sessional_staff.first_name

#     def save(self, *args, **kwargs):
#         self.first_name = self.sessional_staff.first_name
#         super().save(*args, **kwargs)

class JobListing(models.Model):
    unit_name = models.TextField()
    course_description = models.TextField()
    required_qualification = models.CharField(max_length=100)
    teaching_materials = models.CharField(max_length=100)
    session_times = models.CharField(max_length=100)
    responsibilities = models.CharField(max_length=100)
    benefits = models.CharField(max_length=100)

    def __str__(self):
        return self.unit_name

class CreateJob(models.Model):
    UnitName = models.CharField(max_length=255)
    course_description = models.TextField(max_length=255 , null=True)
    required_qualification = models.CharField(max_length=255)
    teaching_materials = models.CharField(max_length=255)
    session_times = models.CharField(max_length=255)
    responsibilities = models.TextField()
    benefits = models.TextField()
    