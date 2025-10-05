# mysite1/myapp1/models.py
from django.db import models
from django.core.validators import RegexValidator, EmailValidator

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True)
    profession = models.CharField(max_length=100, blank=True)
    phone_validator = RegexValidator(
        regex=r'^\+?\d{7,15}$',
        message="Phone must be 7–15 digits, optional leading '+'."
    )
    tel_number = models.CharField(max_length=16, validators=[phone_validator], verbose_name="Telephone")
    email = models.EmailField(unique=True, validators=[EmailValidator()])

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["email"]),
        ]

    def __str__(self):
        return f"{self.name} ({self.email})"