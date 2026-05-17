from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [

        ('core', '0036_add_ese_guide_fields'),

    ]

    operations = [

        migrations.AddField(

            model_name='studentevaluation',

            name='ese_coord1_submitted_at',

            field=models.DateTimeField(blank=True, null=True),

        ),

        migrations.AddField(

            model_name='studentevaluation',

            name='ese_coord2_submitted_at',

            field=models.DateTimeField(blank=True, null=True),

        ),

        migrations.AddField(

            model_name='studentevaluation',

            name='ese_final',

            field=models.IntegerField(blank=True, null=True),

        ),

    ]