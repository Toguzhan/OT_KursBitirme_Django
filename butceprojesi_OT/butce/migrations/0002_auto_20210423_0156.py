# Generated by Django 3.2 on 2021-04-22 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('butce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='butce.category')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='butce.project')),
            ],
        ),
        migrations.DeleteModel(
            name='Expence',
        ),
    ]
