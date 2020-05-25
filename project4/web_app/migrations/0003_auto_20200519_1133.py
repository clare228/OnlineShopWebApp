# Generated by Django 2.0.3 on 2020-05-19 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0002_auto_20200519_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_name', models.CharField(max_length=100)),
                ('set_price', models.FloatField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='items',
            name='sets',
            field=models.ManyToManyField(blank=True, null=True, related_name='set', to='web_app.Group'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='colour',
            name='colour_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_name',
            field=models.CharField(max_length=100),
        ),
    ]
