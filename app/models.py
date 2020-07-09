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
        ("n/a", "Not tested")
    ]
    GENOTYPE_CHOICES = [
        ("AA", "AA"),
        ("AS", "AS"),
        ("AC", "AC"),
        ("SS", "SS"),
        ("n/a", "Not tested")
    ]
    TEST_STATUS_CHOICES = [
        ("positive", "Positive"),
        ("negative", "Negative"),
        ("n/a", "Not Tested"),
    ]

    # Note: basic information shared between users and medical practitioners will be inherited from parent class
    
    # Some user-specific medical information
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default=SEX_CHOICES[0][0])
    blood_type = models.CharField(max_length=3, choices=BLOODTYPE_CHOICES, default=BLOODTYPE_CHOICES[-1][0])
    genotype = models.CharField(max_length=3, choices=GENOTYPE_CHOICES, default=GENOTYPE_CHOICES[-1][0])
    AIDS_status = models.CharField(max_length=10, choices=TEST_STATUS_CHOICES, default=TEST_STATUS_CHOICES[-1][0])
    malaria_status = models.CharField(max_length=10, choices=TEST_STATUS_CHOICES, default=TEST_STATUS_CHOICES[-1][0])
    ebola_status = models.CharField(max_length=10, choices=TEST_STATUS_CHOICES, default=TEST_STATUS_CHOICES[-1][0])
    COVID19_status = models.CharField(max_length=10, choices=TEST_STATUS_CHOICES, default=TEST_STATUS_CHOICES[-1][0])

    # Flag to differentiate users from medical practitioners
    is_practitioner = models.BooleanField(default=False)
