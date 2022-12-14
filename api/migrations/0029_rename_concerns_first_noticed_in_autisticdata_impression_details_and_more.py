# Generated by Django 4.0.4 on 2022-08-04 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_alter_autisticdata_behavioral_and_personal_details_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autisticdata',
            old_name='concerns_first_noticed_in',
            new_name='Impression_Details',
        ),
        migrations.RenameField(
            model_name='autisticdata',
            old_name='developement_evaluation',
            new_name='LLL',
        ),
        migrations.RenameField(
            model_name='autisticdata',
            old_name='general_neurology',
            new_name='LUL',
        ),
        migrations.RenameField(
            model_name='autisticdata',
            old_name='general_neurology_details',
            new_name='RLL',
        ),
        migrations.RenameField(
            model_name='autisticdata',
            old_name='mental_retardation',
            new_name='RUL',
        ),
        migrations.RenameField(
            model_name='autisticdata',
            old_name='neurology',
            new_name='academic_achievements',
        ),
        migrations.RenameField(
            model_name='autisticdata',
            old_name='neurology_evaluation',
            new_name='academic_suggestions_details',
        ),
        migrations.RenameField(
            model_name='autisticdata',
            old_name='present_school_name',
            new_name='adductor_angle_left',
        ),
        migrations.RenameField(
            model_name='autisticdata',
            old_name='school_board',
            new_name='adductor_angle_right',
        ),
        migrations.RenameField(
            model_name='autisticdata',
            old_name='school_medium',
            new_name='ankle_dorsiflexion_left',
        ),
        migrations.RemoveField(
            model_name='autisticdata',
            name='school_comments',
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='ankle_dorsiflexion_right',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='behavior_intervention',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='developemental_intervention',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='developemental_therapy',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='dq_evaluation',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='dysdidocokinesia',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='eclectic_program',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='examination_neurology',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='examination_neurology_details',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='fnf_test',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='hearing_deficit_details',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='investigations',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='investigations_details',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='iq_evaluation',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='learning_difference',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='motor_details',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='plan_reference',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='popliteal_angle',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='pre_primary_school_Board',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='pre_primary_school_Comments',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='pre_primary_school_Medium',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='pre_primary_school_Name',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='prensent_school_Board',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='prensent_school_Comments',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='prensent_school_Medium',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='prensent_school_Name',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='primary_school_Board',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='primary_school_Comments',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='primary_school_Medium',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='primary_school_Name',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='remedial_intervention_details',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='secondary_school_Board',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='secondary_school_Comments',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='secondary_school_Medium',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='secondary_school_Name',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='speech_lang_evaluation',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='sq_evaluation',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='visual_deficits_details',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='autisticdata',
            name='height',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='autisticdata',
            name='weight',
            field=models.TextField(default='', null=True),
        ),
    ]
