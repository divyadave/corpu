from django.db import models

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


class Unit(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


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