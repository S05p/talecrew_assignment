from django.db import models
from talecrew_assignment.settings import AUTH_USER_MODEL


class Post(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL,related_name='post',on_delete=models.PROTECT)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=60000)
    price = models.IntegerField()

    def __str__(self):
        return self.title

class Coupon_publish(models.Model):
    post = models.ForeignKey(Post,related_name='coupon_publish',on_delete=models.CASCADE)
    used_from = models.DateField()
    used_to = models.DateField()
    discount = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self):
        return str(self.post) + str(self.discount) + str('퍼센트 할인')