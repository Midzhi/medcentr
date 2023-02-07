from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name="Город")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Speciality(models.Model):
    name = models.CharField(max_length=255, verbose_name="Специалисты")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"
