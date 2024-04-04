from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    # on_delete = models.CASCADE意思是当删除user时，user的profile也被删除。级联。
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
