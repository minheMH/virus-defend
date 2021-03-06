# Generated by Django 2.2.3 on 2020-02-06 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(choices=[(1, '良好'), (2, '疑似'), (3, '确诊')], default='身体健康状态')),
                ('temp', models.CharField(default='体温', max_length=50)),
                ('place', models.CharField(default='所在区域', max_length=60)),
            ],
        ),
    ]
