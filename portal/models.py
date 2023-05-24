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

    class Meta:
        abstract = True


class PermanentStaff(Staff):
    units = models.ManyToManyField('Unit', related_name='permanent_staff')


class SessionalStaff(Staff):
    units = models.ManyToManyField('Unit', related_name='sessional_staff')

class SessionalStaffUser(models.Model):
    sessional_staffID = models.PrimaryKey(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    phoneno = models.CharField(max_length=10)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    education = models.CharField(max_length=255)
    certification = models.CharField(max_length=255)
    work_experience = models.TextField()
    week_availability = models.CharField(max_length=255)
    days_of_week = models.CharField(max_length=255)
    timing = models.TimeField()
    preferred_unit = models.CharField(max_length=255)
    preferred_location = models.CharField(max_length=255)
    preferred_teaching_styles = models.CharField(max_length=255)


class Unit(models.Model):
    UnitName = models.CharField(max_length=255)
    CourseDescription = models.TextField(max_length=255)
    RequiredQualification = models.CharField(max_length=255)
    teachingMaterials = models.CharField(max_length=255)
    sessionTimes = models.CharField(max_length=255)
    lecturer = models.CharField(max_length=255)
    lecturerEmail = models.CharField(max_length=255)
    

    def __str__(self):
        return self.Unitname


class SessionalApplication(models.Model):
    sessional_staff = models.ForeignKey(SessionalStaff, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    preferences = models.TextField()

class Availibility(models.Model):
    casual_id = models.ForeignKey(SessionalStaff, on_delete=models.CASCADE)
    day_of_the_week = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    id = models.AutoField(primary_key=True, default=999)

    def __str__(self) -> str:
        return f"{self.casual_id}"

class joblisting(models.Model):
    jobID = models.PrimaryKey(SessionalStaff,on_delete=models.CASCADE)
    tutor