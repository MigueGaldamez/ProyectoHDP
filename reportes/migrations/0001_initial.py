# Generated by Django 2.2.13 on 2020-06-21 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantPruebasRealizadas', models.IntegerField()),
                ('cantPruebasPos', models.IntegerField()),
                ('sospechosos', models.IntegerField()),
                ('fechaRegistrado', models.DateTimeField()),
                ('fechaTomado', models.DateTimeField()),
                ('fechaEditado', models.DateTimeField()),
                ('estado', models.IntegerField()),
                ('cantFemenino', models.IntegerField()),
                ('cantMasculino', models.IntegerField()),
                ('edad0_9', models.IntegerField()),
                ('edad10_19', models.IntegerField()),
                ('edad20_39', models.IntegerField()),
                ('edad40_59', models.IntegerField()),
                ('edad60_79', models.IntegerField()),
                ('edad80', models.IntegerField()),
                ('comentario', models.CharField(max_length=200)),
            ],
        ),
    ]