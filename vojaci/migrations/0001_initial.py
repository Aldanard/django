# Generated by Django 4.0.4 on 2022-04-16 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ceta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(help_text='Zadejte název čety', max_length=50, unique=True, verbose_name='Název čety')),
                ('dustojnik', models.CharField(help_text='Zadejte název velícího důstojníka', max_length=50, verbose_name='Název velícího důstojníka')),
            ],
            options={
                'ordering': ['nazev'],
            },
        ),
        migrations.CreateModel(
            name='Mesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(help_text='Zadejte název města', max_length=50, verbose_name='Název města')),
            ],
            options={
                'ordering': ['nazev'],
            },
        ),
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(help_text='Zadejte jméno vojáka', max_length=50, verbose_name='Jméno vojáka')),
                ('prijmeni', models.CharField(help_text='Zadejte příjmení vojáka', max_length=50, verbose_name='Příjmení vojáka')),
                ('hodnost', models.CharField(help_text='Zadejte hodnost vojáka', max_length=50, verbose_name='Hodnost vojáka')),
                ('datumN', models.DateField()),
                ('bydliste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vojaci.mesto')),
                ('ceta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vojaci.ceta')),
            ],
            options={
                'ordering': ['prijmeni'],
            },
        ),
        migrations.CreateModel(
            name='Rota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(help_text='Zadejte název roty', max_length=50, unique=True, verbose_name='Název roty')),
                ('zamereni', models.CharField(help_text='Zadejte zaměření roty', max_length=50, verbose_name='Zeměření roty')),
                ('vedouci', models.CharField(help_text='Zadejte jméno vedoucího roty', max_length=50, verbose_name='Jméno vedoucího')),
            ],
            options={
                'ordering': ['nazev'],
            },
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(help_text='Zadejte název státu', max_length=50, unique=True, verbose_name='Název státu')),
                ('zkratka', models.CharField(help_text='Zadejte zkratku státu', max_length=2, unique=True, verbose_name='Zkratka státu')),
            ],
            options={
                'ordering': ['nazev'],
            },
        ),
        migrations.CreateModel(
            name='Vyznamenani',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(help_text='Zadejte název vyznamenání', max_length=50, verbose_name='Název vyznamenání')),
                ('rokU', models.IntegerField(help_text='Zadejte rok udělení', max_length=4, verbose_name='Roku udělení')),
                ('popis', models.TextField(blank=True, help_text='Popište vyznamenání', null=True, verbose_name='Popis vyznamenání')),
                ('osoba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vojaci.osoba')),
            ],
            options={
                'ordering': ['nazev'],
            },
        ),
        migrations.AddField(
            model_name='mesto',
            name='stat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vojaci.stat'),
        ),
        migrations.AddField(
            model_name='ceta',
            name='rota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vojaci.rota'),
        ),
    ]