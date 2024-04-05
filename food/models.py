from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Item(models.Model):
    """
    thie def __str__ 相当于toString()
    """

    def __str__(self):
        return self.item_name

    # 把django的user model作为本model的foreign key
    # default=1 表示如果没有为该字段指定值，则默认为 1。
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    item_name = models.CharField(max_length=200)
    item_description = models.TextField()
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,
                                  default='https://images.ctfassets.net/84wm3hhxw4gx/0sxerdVddcgpnd69VcMsx/414cb6a014fc90e5d96e07fef8022ccf/foodplaceholder.png')

    # 用途：重定向到一个新页面
    # 这里想让用户在创建某个food item时，让django重定向到该项目的detail
    def get_absolute_url(self):
        return reverse('food:detail', kwargs={'pk': self.pk})