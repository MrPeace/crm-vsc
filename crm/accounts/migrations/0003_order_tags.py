# Generated by Django 4.1.1 on 2022-09-28 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_tag_order_customer_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tags',
            field=models.ManyToManyField(to='accounts.tag'),
        ),
    ]
