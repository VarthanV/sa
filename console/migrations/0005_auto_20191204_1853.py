# Generated by Django 2.2 on 2019-12-04 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0004_auto_20191128_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester',
            name='semster',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='tcred',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='exam',
        ),
        migrations.AddField(
            model_name='semester',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='console.Subject'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='sem',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subcred',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='1', max_length=1),
        ),
    ]
