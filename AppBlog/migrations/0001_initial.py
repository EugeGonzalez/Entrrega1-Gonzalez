# Generated by Django 4.0.5 on 2022-07-12 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=30)),
                ('tipo_usuario', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CrearUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=60)),
                ('fecha_nacimiento', models.DateField()),
                ('contraseña', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='InicioSesion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=30)),
            ],
        ),
    ]
