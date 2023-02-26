# Generated by Django 3.2.9 on 2023-02-24 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_auto_20230224_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='complexity',
            field=models.IntegerField(choices=[(1, 'Simple'), (2, 'Moderate'), (3, 'High'), (4, 'Advanced'), (5, 'Extreme')]),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.IntegerField(choices=[(1, 'Open'), (2, 'Picked'), (3, 'Completed')], default=1),
        ),
        migrations.CreateModel(
            name='Assign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.issue')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
