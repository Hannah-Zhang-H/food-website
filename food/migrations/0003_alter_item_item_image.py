# Generated by Django 5.0.3 on 2024-04-01 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0002_item_item_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="item_image",
            field=models.CharField(
                default="https://images.ctfassets.net/84wm3hhxw4gx/0sxerdVddcgpnd69VcMsx/414cb6a014fc90e5d96e07fef8022ccf/foodplaceholder.png",
                max_length=500,
            ),
        ),
    ]
