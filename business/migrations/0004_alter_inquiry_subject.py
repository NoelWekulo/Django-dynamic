# Generated by Django 5.1.2 on 2024-11-16 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_inquiry_subject_alter_portfolio_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='subject',
            field=models.CharField(default='General Inquiry', max_length=55),
        ),
    ]
