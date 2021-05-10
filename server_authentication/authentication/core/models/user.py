from django.contrib.auth.models import AbstractUser
from django.db import models


class Gender(models.Model):
    title = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return self.title


class User(AbstractUser):
    uid = models.CharField(unique=True, null=True, blank=True, max_length=255)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)

    REQUIRED_FIELDS = ["email", "uid"]

    def __str__(self):
        return self.username

    class Meta:
        db_table = "User"

        def __str__(self):
            return "{0}: {1}".format(self.__class__.__name__, self.name)

    # def save(self, *args, **kwargs):

    #     if not self.id:
    #         self.uid = str(uuid.uuid4().hex)

    #     super(User, self).save(*args, **kwargs)
