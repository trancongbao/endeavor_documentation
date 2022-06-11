from django.db import models
from django.contrib.auth.models import User


class Deck(models.Model):
    # TODO: name should be unique, non blank (MinLengthValidator, ModelForm)
    name = models.CharField(unique=True, max_length=100)
    # Deck-User relationship can be extracted from StudiedCard for non-empty deck only
    users = models.ManyToManyField(User)
    order = models.PositiveIntegerField(unique=True, null=True, blank=True)

    class Meta:
        verbose_name = "Deck"
        verbose_name_plural = "Decks"

    def __str__(self):
        return self.name


class Word(models.Model):
    text = models.TextField(max_length=100)
    part_of_speech = models.TextField(max_length=10, null=True, blank=True)  # TODO
    phonetic = models.TextField(max_length=100, null=True, blank=True)  # TODO
    definition = models.TextField(max_length=500)
    # TODO: delete unused media
    # TODO: image and video should probably be mutually exclusive
    image = models.ImageField(upload_to="image", null=True, blank=True)
    video = models.FileField(upload_to="video", null=True, blank=True)  # TODO

    def __str__(self):
        return self.text + " :: " + self.definition[0:100]

    class Meta:
        unique_together = ("text", "definition")


class Card(models.Model):
    user = models.ManyToManyField(User, through="StudiedCard")
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name="cards")
    # TODO: order in text, reordering in admin?
    order = models.PositiveIntegerField(unique=True, null=True, blank=True)
    front_text = models.TextField(max_length=500)
    front_audio = models.FileField(upload_to="audio", null=True, blank=True)
    words = models.ManyToManyField(Word, through="WordInCard")

    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"

    def __str__(self):
        return self.front_text[0:100]


# TODO: ManyToManyField
class WordInCard(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ("card", "word")


class StudiedCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    study_date = models.DateField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ("user", "card")
