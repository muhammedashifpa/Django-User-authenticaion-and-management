from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Orders(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE ,blank=True,null=True)
    order_date = models.DateTimeField(default = timezone.now)
    item_name = models.CharField(max_length=30)
    price = models.IntegerField()
    def __str__(self):
        return self.order_id
    class Meta:
        ordering = ['order_date']

