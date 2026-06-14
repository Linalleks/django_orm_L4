from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField('Название', max_length=200)
    title_en = models.CharField('Название (англ)', max_length=200)
    title_jp = models.CharField('Название (яп)', max_length=200)
    description = models.TextField()
    image = models.ImageField('Изображение', upload_to="images", null=True, blank=True)
    previous_evolution = models.ForeignKey('self', verbose_name='Из кого эволюционировал', on_delete=models.SET_NULL,
                                           null=True, blank=True, related_name='next_evolutions')

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон',
                                on_delete=models.CASCADE, related_name='entities')
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')
    appeared_at = models.DateTimeField('Дата и время появления')
    disappeared_at = models.DateTimeField('Дата и время исчезновения')
    level = models.IntegerField('Уровень', default=0)
    health = models.IntegerField('Здоровье', default=0)
    strength = models.IntegerField('Атака', default=0)
    defence = models.IntegerField('Защита', default=0)
    stamina = models.IntegerField('Выносливость', default=0)

    class Meta:
        verbose_name = 'Особь покемонов'
        verbose_name_plural = 'Особи покемонов'

    def __str__(self):
        return f"{self.pokemon.title_ru} - {self.lat} : {self.lon}"
