from django.db import models

class Drink(models.Model):
    ingridient = models.CharField(max_length=120, db_index=True)
    calories = models.TextField(blank=True, db_index=True)

    def __str__(self):
        return self.ingridient



