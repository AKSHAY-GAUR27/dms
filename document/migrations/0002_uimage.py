# Generated by Django 2.2 on 2019-05-21 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.TextField()),
                ('Pic', models.ImageField(upload_to='static/images')),
                ('Receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.AddUser')),
            ],
        ),
    ]
