# Generated by Django 4.0 on 2022-05-07 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_alter_course_icon_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='icon',
            field=models.ImageField(default='/static/course_images/img.jpeg', upload_to='course_images'),
        ),
    ]