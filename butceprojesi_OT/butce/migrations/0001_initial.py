# Generated by Django 3.2 on 2021-04-22 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('butce', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Expence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='butce.category')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='butce.project')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='butce.project'),
        ),
    ]
