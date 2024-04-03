from django import forms
from .models import Item


# 告诉Django，这个form要用Item这个model
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        """
        下面这些变量是我实际想要用户输入的内容
        """
        fields = ['item_name', 'item_price', 'item_description', 'item_image']
