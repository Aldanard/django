from django.db import models


class Rota(models.Model):
    nazev = models.CharField(max_length=50, unique=True, verbose_name='Název roty', help_text='Zadejte název roty')
    zamereni = models.CharField(max_length=50, verbose_name='Zeměření roty', help_text='Zadejte zaměření roty')
    vedouci = models.CharField(max_length=50, verbose_name='Jméno vedoucího', help_text='Zadejte jméno vedoucího roty')

    class Meta:
        ordering = ['nazev']

    def __str__(self):
        return self.nazev


class Stat(models.Model):
    nazev = models.CharField(max_length=50, unique=True, verbose_name='Název státu', help_text='Zadejte název státu')
    zkratka = models.CharField(max_length=2, unique=True, verbose_name='Zkratka státu', help_text='Zadejte zkratku státu')

    class Meta:
        ordering = ['nazev']

    def __str__(self):
        return self.nazev


class Ceta(models.Model):

    nazev = models.CharField(max_length=50, unique=True, verbose_name='Název čety', help_text='Zadejte název čety')
    dustojnik = models.CharField(max_length=50, verbose_name='Název velícího důstojníka', help_text='Zadejte název velícího důstojníka')
    rota = models.ForeignKey(Rota, on_delete=models.CASCADE)

    class Meta:
        ordering = ['nazev']

    def __str__(self):
        return f'Rota {self.rota.nazev} - Četa {self.nazev}'

class Mesto(models.Model):
    nazev = models.CharField(max_length=50, verbose_name='Název města', help_text='Zadejte název města')
    stat = models.ForeignKey(Stat, on_delete=models.CASCADE)

    class Meta:
            ordering = ['nazev']

    def __str__(self):
            return f'{self.nazev}, {self.stat.zkratka}'

class Osoba(models.Model):
    jmeno = models.CharField(max_length=50, verbose_name='Jméno vojáka', help_text='Zadejte jméno vojáka')
    prijmeni = models.CharField(max_length=50, verbose_name='Příjmení vojáka', help_text='Zadejte příjmení vojáka')
    hodnost = models.CharField(max_length=50, verbose_name='Hodnost vojáka', help_text='Zadejte hodnost vojáka')
    datumN = models.DateField()
    bydliste = models.ForeignKey(Mesto, on_delete=models.CASCADE)
    ceta = models.ForeignKey(Ceta, on_delete=models.CASCADE)

    class Meta:
        ordering = ['prijmeni']

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'


class Vyznamenani(models.Model):
    nazev = models.CharField(max_length=50, verbose_name='Název vyznamenání', help_text='Zadejte název vyznamenání')
    rokU = models.IntegerField(max_length=4, verbose_name='Roku udělení', help_text='Zadejte rok udělení')
    popis = models.TextField (blank= True, null=True, verbose_name='Popis vyznamenání', help_text='Popište vyznamenání')
    osoba = models.ForeignKey (Osoba, on_delete=models.CASCADE)

    class Meta:
        ordering = ['nazev']

    def __str__(self):
        f'{self.nazev} ({self.osoba.jmeno} {self.osoba.prijmeni})'

