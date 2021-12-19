from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyUserManager(BaseUserManager):
    def create_user(self, email,
                    username,
                    first_name,
                    last_name,
                    # date_of_birth, 
                    password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            # date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,
                         username,
                         first_name,
                         last_name,
                        #  date_of_birth, 
                         password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            username= username,
            first_name= first_name,
            last_name = last_name,
            password=password,
            # date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
    username = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    
    uploadpath = 'profiles/'
    image = models.ImageField(blank=True, upload_to=uploadpath, width_field=300 , height_field=500 )
    
    date_of_birth = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class MyUserLoc(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, parent_link=False,primary_key = True)
    # username = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return str(self.user)

class UserHistory(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, parent_link=False)
    search_item_name = models.IntegerField()
