from django.db import models

# Create your models here.
class Wallet(models.Model):
    #style has unique id 
    style = models.AutoField(primary_key=True,unique=True)
    #name is a string 
    name = models.CharField(max_length=20)
    #creating a tuple of sizes
    SIZES = (
        ('T', 'Tiny'),
        ('N', 'Normal'),
        ('H', 'Huge'),
        )
    size = models.CharField(max_length=1, choices=SIZES)
    #creating a tuple of colors
    COLORS = (
        ('B', 'Black'),
        ('G', 'Beige'),
        ('W', 'White'),
        ('R', 'Red')
        )
    color = models.CharField(max_length=1, choices=COLORS)
    #creating tuple of card slots
    l1 = range(2,16)
    l2 = range(2,16)
    l = zip(l1,l2)
    card_slots = models.IntegerField(choices=l)
    #creating tuple for YES/NO
    YN = [('Y', 'Yes'),('N','No')]
    id_slot = models.CharField(max_length=1, choices=YN)
    coin_pocket = models.CharField(max_length=1, choices=YN)
    #creating tuple for money slots
    D = [(1,1),(2,2)]
    money_slots = models.SmallIntegerField(choices=D)
    embossed_name = models.CharField(max_length = 10, 
                    help_text = "Not more than 10 characters")

    #to make object pretty
    def __str__(self):
        return str(self.style) + " " + self.name
