from django.db import models

# Create your models here.
class join_us_user(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    linkedin = models.URLField()

    class Meta:
        db_table = "Join_users"