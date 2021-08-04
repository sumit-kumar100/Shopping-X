# Generated by Django 3.2.5 on 2021-07-28 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Eshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WomensTopWear',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eshop.product')),
            ],
        ),
        migrations.CreateModel(
            name='TrendingProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eshop.product')),
            ],
        ),
        migrations.CreateModel(
            name='MensTopWear',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eshop.product')),
            ],
        ),
        migrations.CreateModel(
            name='DealOfDay',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eshop.product')),
            ],
        ),
    ]