# Generated by Django 3.2.9 on 2023-02-24 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='complexity',
            field=models.IntegerField(choices=[(1, 'Elementary'), (2, 'Simple'), (3, 'Moderate'), (4, 'High'), (5, 'Advanced'), (6, 'Extreme')]),
        ),
        migrations.AlterField(
            model_name='issue',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.IntegerField(choices=[(1, 'Open'), (2, 'Picked'), (3, 'Completed')], default=0),
        ),
    ]