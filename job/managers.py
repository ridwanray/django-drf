from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where username is the unique identifiers
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given username and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        user = self.create_user(email, password, **extra_fields)
        user.role = ["ADMIN"]
        user.save()
        
        return user
    
    def create_app_user(self, email, password, **extra_fields):
            if not email:
                raise ValueError(_("The Email must be set"))
            email = self.normalize_email(email)
            user = self.model(email=email, password = password, is_active=True, verified=True,  **extra_fields)
            user.save()
            return user

