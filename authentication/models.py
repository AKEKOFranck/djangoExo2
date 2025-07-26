from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    age = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(10),
            MaxValueValidator(60),
        ],
        verbose_name="Âge de l'utilisateur",
        help_text="L'âge doit être compris entre 10 et 60 ans"
    )
    
    def __str__(self):
        return self.username