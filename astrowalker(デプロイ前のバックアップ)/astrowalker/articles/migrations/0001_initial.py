# Generated by Django 2.2.5 on 2019-09-21 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
                ('tag', models.CharField(choices=[('0', '内容がない'), ('1', '科学'), ('2', '思考')], max_length=20)),
            ],
        ),
    ]
