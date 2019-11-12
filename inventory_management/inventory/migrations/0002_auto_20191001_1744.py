# Generated by Django 2.2.4 on 2019-10-01 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='desktop',
            old_name='priice',
            new_name='Price',
        ),
        migrations.RenameField(
            model_name='laptop',
            old_name='priice',
            new_name='Price',
        ),
        migrations.RenameField(
            model_name='mobile',
            old_name='priice',
            new_name='Price',
        ),
        migrations.AlterField(
            model_name='desktop',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item ready to br purchased'), ('SOLD', 'Item Sold'), ('RESTOCKING', 'Item restocking in few days')], default='SOLD', max_length=100),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item ready to br purchased'), ('SOLD', 'Item Sold'), ('RESTOCKING', 'Item restocking in few days')], default='SOLD', max_length=100),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item ready to br purchased'), ('SOLD', 'Item Sold'), ('RESTOCKING', 'Item restocking in few days')], default='SOLD', max_length=100),
        ),
    ]
