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

    # Note: basic information shared between users and medical practitioners will be inherited from parent class
    
    # Some user-specific medical information
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default="")
    blood_type = models.CharField(max_length=3, choices=BLOODTYPE_CHOICES, default="")
    genotype = models.CharField(max_length=2, choices=GENOTYPE_CHOICES, default="")
    # The required default values for the Boolean fields are set to False because false-negatives
    # less risky than false-positives in the context of patient information reporting.
    has_aids = models.BooleanField(default=False)
    has_malaria = models.BooleanField(default=False)
    has_ebola = models.BooleanField(default=False)
    has_covid19 = models.BooleanField(default=False)

    # Flag to differentiate users from medical practitioners
    is_practitioner = models.BooleanField(null=False)
