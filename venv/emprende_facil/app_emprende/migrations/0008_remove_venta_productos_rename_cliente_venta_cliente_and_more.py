# Generated by Django 5.0.2 on 2024-04-03 01:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_emprende', '0007_venta_ventadetalle_venta_productos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='productos',
        ),
        migrations.RenameField(
            model_name='venta',
            old_name='Cliente',
            new_name='cliente',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='total',
        ),
        migrations.AddField(
            model_name='venta',
            name='cantidad',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='fecha_venta',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_emprende.producto'),
        ),
        migrations.AddField(
            model_name='venta',
            name='total_ganar',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='total_venta',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='VentaDetalle',
        ),
    ]
