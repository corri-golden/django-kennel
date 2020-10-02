from django.db import models

class Kennel (models.Model):

    title = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("kennel")
        verbose_name_plural = ("kennels")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("kennel_detail", kwargs={"pk": self.pk})
