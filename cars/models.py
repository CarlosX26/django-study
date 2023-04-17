from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=64)
    color = models.CharField(max_length=32)
    year = models.IntegerField()

    def __repr__(self) -> str:
        return f"<Car ({self.id}) - {self.model}>"
