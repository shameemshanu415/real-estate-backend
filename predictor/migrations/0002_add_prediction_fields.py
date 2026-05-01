from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='prediction',
            name='property_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
