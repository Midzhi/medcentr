from django.db import models

from users.models import User

from mainapp.models import City, Speciality


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="doctor")
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name="doctors")
    speciality = models.ForeignKey(
        Speciality, on_delete=models.PROTECT, related_name="doctors"
    )
    working_place = models.CharField(max_length=255, verbose_name="Место работы")
    propic = models.ImageField(
        upload_to="propics/", null=True, blank=True, verbose_name="Фотография"
    )

    def __str__(self) -> str:
        return f"{self.user.full_name} -- {self.city.name} - {self.speciality.name}"

    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Доктора"
