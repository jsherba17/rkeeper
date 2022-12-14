# Generated by Django 4.1.1 on 2022-09-19 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0003_order_food_alter_food_price_alter_quantity_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalSum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='sum',
        ),
        migrations.AlterField(
            model_name='order',
            name='percent',
            field=models.IntegerField(default=15),
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cafe.totalsum'),
        ),
    ]
