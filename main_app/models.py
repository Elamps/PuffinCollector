from django.db import models
from django.urls import reverse

FISH = (
    ('E', 'Eels'),
    ('H', 'Herring'),
    ('C', 'Capelin'),
    ('S', 'Crustaceans')
)

class Puffin(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'puffin_id': self.id})

class Feeding(models.Model):
    date = models.DateField('Fishing date')
    fish = models.CharField(
         max_length=1,
         choices=FISH,
         default=FISH[0][0]
    )
    puffin = models.ForeignKey(Puffin, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_fish_display()} on {self.date}"
    class Meta:
        ordering = ['-date']