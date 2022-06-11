from django.contrib import admin
from .models import Deck, Card, Word, WordInCard, StudiedCard

admin.site.register(Deck)
admin.site.register(Card)
admin.site.register(Word)
admin.site.register(WordInCard)
admin.site.register(StudiedCard)
