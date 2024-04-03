from django.db import models


# Create your models here.
class Item(models.Model):
    """
    thie def __str__ 相当于toString()
    """

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_description = models.TextField()
    item_price = models.IntegerField()
    # item_image = models.ImageField(upload_to='food/static/food/image/', default='https://images.ctfassets.net/84wm3hhxw4gx/0sxerdVddcgpnd69VcMsx/414cb6a014fc90e5d96e07fef8022ccf/foodplaceholder.png'      )
    item_image = models.CharField(max_length=500,
                                  default='https://images.ctfassets.net/84wm3hhxw4gx/0sxerdVddcgpnd69VcMsx/414cb6a014fc90e5d96e07fef8022ccf/foodplaceholder.png')
