# Generated by Django 5.0.3 on 2024-03-31 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="item_image",
            field=models.ImageField(
                default="https://images.ctfassets.net/84wm3hhxw4gx/0sxerdVddcgpnd69VcMsx/414cb6a014fc90e5d96e07fef8022ccf/foodplaceholder.png",
                upload_to="food/static/food/image/",
            ),
        ),
    ]