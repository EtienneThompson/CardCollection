from django.db import models


class Card(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_name = models.CharField(max_length=200)
    card_set = models.ForeignKey("Set", on_delete=models.DO_NOTHING)
    card_number = models.IntegerField()
    card_price = models.FloatField()


class Set(models.Model):
    set_id = models.AutoField(primary_key=True)
    set_name = models.CharField(max_length=200)
    set_cards = models.ManyToManyField(Card)


class Wishlist(models.Model):
    wishlist_id = models.AutoField(primary_key=True)
    wishlist_cards = models.ManyToManyField("Card")


class Quantity(models.Model):
    collection = models.ForeignKey("Collection", on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    card_quantity = models.IntegerField()


class Collection(models.Model):
    collection_id = models.AutoField(primary_key=True)
    collection_name = models.CharField(max_length=200)
    collection_cards = models.ManyToManyField(Card, through=Quantity)
    collection_user = models.ForeignKey("User", on_delete=models.CASCADE)


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=64)
    auth_token = models.CharField(unique=True, max_length=200)
    last_online = models.DateTimeField()
    wishlist = models.OneToOneField(
        "Wishlist", on_delete=models.CASCADE)
