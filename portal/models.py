from django.db import models


class Unit(models.Model):
    UNIT_CHOICES = (
        ('COS60001', 'COS60001 INTRO TO DATA SCIENCE'),
        ('COS60002', 'COS60002 INTRO TO COMPUTER SCIENCE'),
        ('COS60003', 'COS60003 DATABASE SYSTEMS'),
    )

    unitName = models.CharField(max_length=8, choices=UNIT_CHOICES)
    courseDescription = models.TextField()
    requiredQualification = models.CharField(max_length=100)
    teachingMaterials = models.CharField(max_length=200)
    sessionTimes = models.CharField(max_length=100)
    lecturer = models.CharField(max_length=100)
    lecturerEmail = models.EmailField()

    def __str__(self):
        return self.unitName
