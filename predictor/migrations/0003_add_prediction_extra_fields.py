from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0002_add_prediction_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='bathrooms',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='prediction',
            name='floors',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='prediction',
            name='year_built',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prediction',
            name='condition',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='prediction',
            name='garage',
            field=models.BooleanField(default=False),
        ),
    ]
