from django.db import models
from accounts.models import User
from posts.models import Post, Coupon_publish


# Create your models here.

class Coupon(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    used_from = models.DateField()
    used_to = models.DateField()
    discount = models.IntegerField()
    used = models.BooleanField(default=True)
    publish_pk = models.IntegerField()

    def __str__(self):
        return str(self.post)

