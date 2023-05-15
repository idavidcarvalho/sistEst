# Generated by Django 4.2.1 on 2023-05-15 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('idUsuario', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=300)),
                ('cpf', models.CharField(max_length=11)),
                ('num_CNH', models.CharField(max_length=15, null=True)),
                ('validade_CNH', models.DateField(help_text='Formato <em>YYYY-MM-DD</em>', null=True)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=300, null=True)),
            ],
        ),
    ]
