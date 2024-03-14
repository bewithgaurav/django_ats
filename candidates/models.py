from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    years_of_exp = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    current_salary = models.DecimalField(max_digits=10, decimal_places=2)
    expected_salary = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="Applied")