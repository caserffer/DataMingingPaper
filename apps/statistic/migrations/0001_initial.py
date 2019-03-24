# Generated by Django 2.0.1 on 2019-03-25 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AffDistribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affiliation', models.CharField(max_length=220, verbose_name='机构名称')),
                ('country', models.CharField(max_length=20, verbose_name='所属国家')),
                ('count', models.IntegerField(default=0, verbose_name='发表频数')),
            ],
            options={
                'verbose_name': '机构国家分布表',
                'verbose_name_plural': '机构国家分布表',
            },
        ),
    ]
