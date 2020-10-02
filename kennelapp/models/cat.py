from django.db import models
from .kennel import Kennel
from .caretaker import Caretaker 
 
class Cat(models.Model):

    Name = models.CharField(max_length=50)
    Specie = models.CharField(max_length=50)
    Owner = models.CharField(max_length=50)
    Admitted = models.CharField(max_length=50)
    Location = models.ForeignKey(Kennel, on_delete=models.CASCADE)
    Caretaker = models.ForeignKey(Caretaker, on_delete=models.CASCADE)


    class Meta:
        verbose_name = ("cat")
        verbose_name_plural = ("cats")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cat_detail", kwargs={"pk": self.pk})
