from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Basic information shared between users and medical practitioners
    

    # User-specific medical information (fields are set to nullable to enable medical practitioners to be persisted on this table also)

    # Flag to differentiate users from medical practitioners
    pass