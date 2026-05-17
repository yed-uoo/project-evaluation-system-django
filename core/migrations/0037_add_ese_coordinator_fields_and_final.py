import django.core.validators

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [

        ('core', '0036_add_ese_guide_fields'),

    ]

    operations = [

        migrations.AddField(

            model_name='studentevaluation',

            name='ese_coord1_submitted',

            field=models.BooleanField(default=False),

        ),

        migrations.AddField(

            model_name='studentevaluation',

            name='ese_coord1_submitted_at',

            field=models.DateTimeField(blank=True, null=True),

        ),

        migrations.AddField(

            model_name='studentevaluation',

            name='ese_coord1_viva',

            field=models.IntegerField(

                default=0,

                validators=[

                    django.core.validators.MinValueValidator(0),

                    django.core.validators.MaxValueValidator(25)

                ]

            ),

        ),

        migrations.AddField(

            model_name='studentevaluation',

            name='ese_coord2_submitted',

            field=models.BooleanField(default=False),

        ),

        migrations.AddField(

            model_name='studentevaluation',

            name='ese_coord2_submitted_at',

            field=models.DateTimeField(blank=True, null=True),

        ),

        migrations.AddField(

            model_name='studentevaluation',

            name='ese_coord2_viva',

            field=models.IntegerField(

                default=0,

                validators=[

                    django.core.validators.MinValueValidator(0),

                    django.core.validators.MaxValueValidator(25)

                ]

            ),

        ),

        migrations.AddField(

            model_name='studentevaluation',

            name='ese_final',

            field=models.IntegerField(blank=True, null=True),

        ),

    ]