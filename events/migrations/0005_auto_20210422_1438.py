# Generated by Django 3.0.5 on 2021-04-22 11:38

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_remove_imageofevent_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image_ppoi',
            field=versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='images/', verbose_name='ImageofEvent'),
        ),
    ]
