from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    This object model is used to persist both regular users and medical practitioners in a bid to adhere to the DRY principle.
    Further, this provides flexibility for medical practitioners to operate as regular users in future requirements (future-proofing).
    """

    # Some pre-defined field choices
    SEX_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]
    BLOODTYPE_CHOICES = [
        ("O-", "O negative"),
        ("O+", "O positive"),
        ("A-", "A negative"),
        ("A+", "A positive"),
        ("B-", "B positive"),
        ("B+", "B positive"),
        ("AB-", "AB negative"),
        ("AB+", "AB positive"),
    ]
    GENOTYPE_CHOICES = [
        ("AA", "AA"),
        ("AS", "AS"),
        ("AC", "AC"),
        ("SS", "SS"),
    ]
    TEST_STATUS_CHOICES = [
        ("positive", "Positive"),
        ("negative", "Negative"),
        ("n/a", "Not Tested"),
    ]

    # Note: basic information shared between users and medical practitioners will be inherited from parent class
    
    # Some user-specific medical information
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default="")
    blood_type = models.CharField(max_length=3, choices=BLOODTYPE_CHOICES, default="")
    genotype = models.CharField(max_length=2, choices=GENOTYPE_CHOICES, default="")
    AIDS_status = models.CharField(max_length=10, choices=TEST_STATUS_CHOICES, default="")
    malaria_status = models.CharField(max_length=10, choices=TEST_STATUS_CHOICES, default="")
    ebola_status = models.CharField(max_length=10, choices=TEST_STATUS_CHOICES, default="")
    COVID19_status = models.CharField(max_length=10, choices=TEST_STATUS_CHOICES, default="")

    # Flag to differentiate users from medical practitioners
    is_practitioner = models.BooleanField(default=False)


class UserFieldQuestion(models.Model):
    # Kindly add new field choices by appending to the list below
    # This is because the ordering artifact is used in the application logic
    FIELD_CHOICES = [
        ("age", "Age"),
        ("sex", "Sex"),
        ("blood_type", "Blood Type"),
        ("genotype", "Genotype"),
        ("AIDS_status", "AIDS Status"),
        ("malaria_status", "Malaria Status"),
        ("ebola_status", "Ebola Status"),
        ("COVID19_status", "COVID19 Status"),
    ]

    question = models.CharField(max_length=255, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_field = models.CharField(max_length=20, choices=FIELD_CHOICES, default="")
