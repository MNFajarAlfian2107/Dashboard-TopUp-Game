from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    game = models.CharField(max_length=100)
    nominal = models.CharField(max_length=100)
    payment = models.CharField(max_length=100)
    total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.game} - {self.total}"


class Game(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='games/')

    def __str__(self):
        return self.name


class Nominal(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    amount = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.game.name} - {self.amount}"