from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class EntrepreneurManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Le champ Email doit être renseigné')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Entrepreneur(AbstractBaseUser, PermissionsMixin):
    nomEntrepreneure = models.CharField(max_length=100)
    prenomEntrepreneure = models.CharField(max_length=100)
    dateNaissanceEntrepreneure = models.DateField()
    secteurActivite = models.CharField(max_length=100)
    paysActivite = models.CharField(max_length=100)
    regionActivite = models.CharField(max_length=100)
    telephone = models.IntegerField()
    adresse = models.CharField(max_length=255)
    email = models.EmailField(unique=True, default='default@example.com')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='entrepreneur_groups',  # Ajoutez un related_name unique ici
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='entrepreneur_permissions',  # Ajoutez un related_name unique ici
        blank=True
    )

    objects = EntrepreneurManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nomEntrepreneure', 'prenomEntrepreneure']

    def __str__(self):
        return f"{self.prenomEntrepreneure} {self.nomEntrepreneure}"
