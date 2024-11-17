from django.contrib.auth.models import AbstractUser
from django.db import models

class UserType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    user_type = models.ForeignKey(
        UserType, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name="users"
    )
    middle_name = models.CharField("Second Last Name", max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.user_type})" if self.user_type else self.username
