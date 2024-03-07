from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Family(models.Model):
    family_name = models.CharField(max_length=255)

    def __str__(self):
        return self.family_name

    def add_member(self, member):
        pass

    def remove_member(self, member):
        pass

    @classmethod
    def list_members(cls, person):
        family_persons = Person.objects.filter(family=person.family)
        return family_persons
    
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    kindred = models.CharField(max_length=255)
    is_family_admin = models.BooleanField(default=False)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    def __str__(self):
        return F"{self.user.username} in {self.family}'s family"
    