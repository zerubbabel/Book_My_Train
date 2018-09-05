# Generated by Django 2.1 on 2018-08-22 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_remove_book_passengers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Card_Number', models.CharField(max_length=16)),
                ('CVV', models.CharField(max_length=3)),
                ('Names', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.User')),
            ],
        ),
    ]
