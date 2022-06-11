# python
import math
from datetime import timedelta, date

# django
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.db.models import Q
from django.core import serializers
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# project
from endeavorapp.models import Card, Deck, StudiedCard, Word, WordInCard


def home(request):
    return redirect("login/")


def logout_view(request):
    logout(request)
    return redirect("/")


def login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
        login_view.next = request.GET.get("next", "/decks/")
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(login_view.next)
    return render(
        request=request, template_name="endeavorapp/login.html", context={"form": form}
    )


@login_required(login_url="/login/")
def decks(request):
    user = User.objects.get(id=request.user.id)
    decks = user.deck_set.all()
    return render(
        request=request,
        template_name="endeavorapp/decks.html",
        context={"decks": decks},
    )


# TODO: set permission
@login_required(login_url="/login/")
def create_deck(request):
    name = request.POST.get("name")
    deck = Deck(name=name)
    deck.save()
    super_users = User.objects.filter(is_superuser=True)
    deck.users.add(*super_users)
    return redirect("/decks/")


@login_required(login_url="/login/")
def study(request, deck_id):
    user = User.objects.get(id=request.user.id)
    studied_cards = StudiedCard.objects.filter(user=user)  # TODO: deadline
    displayed_cards = [
        _prepare_displayed_card(card.card, card.study_date, card.deadline)
        for card in studied_cards
    ]

    remaining_cards = Card.objects.filter(deck_id=deck_id).exclude(
        id__in=[studied_card.card.id for studied_card in studied_cards]
    )
    displayed_cards.extend([_prepare_displayed_card(card) for card in remaining_cards])

    return render(
        request=request,
        template_name="endeavorapp/study.html",
        context={"cards": displayed_cards},
    )


def _prepare_displayed_card(card, study_date=None, deadline=None):
    displayed_card = {"id": card.id}
    # Front
    displayed_card["front_text"] = card.front_text
    displayed_card["front_audio"] = (
        card.front_audio.url if card.front_audio.name else None
    )

    # Back
    words = []
    for word in card.words.all():
        words.append(
            {
                "text": word.text,
                "definition": word.definition,
                "image": word.image.url if word.image.name else None,
                "video": word.video.url if word.video.name else None,
            }
        )
    displayed_card["words"] = words

    # Intervals
    GRADUATING_INTERVAL = 1
    EASE_PERCENTAGE = 2.5
    INTERVAL_MODIFIER = 1
    EASY_BONUS = 1.3
    HARD_INTERVAL = 1.2
    if study_date == None or deadline <= study_date:  # new/again card
        interval = GRADUATING_INTERVAL
    else:
        interval = (deadline - study_date).days
    displayed_card["hard"] = math.floor(interval * HARD_INTERVAL * INTERVAL_MODIFIER)
    displayed_card["good"] = math.floor(interval * EASE_PERCENTAGE * INTERVAL_MODIFIER)
    displayed_card["easy"] = math.floor(
        interval * EASE_PERCENTAGE * INTERVAL_MODIFIER * EASY_BONUS
    )

    return displayed_card


@login_required(login_url="/login/")
def schedule(request, card_id):
    interval = int(request.GET.get("interval"))
    studied_card, created = StudiedCard.objects.update_or_create(
        user=User.objects.get(id=request.user.id),
        card=Card.objects.get(id=card_id),
        defaults={
            "study_date": date.today(),
            "deadline": date.today() + timedelta(days=interval),
        },
    )
    return HttpResponse(status=204)


def done(request):
    return render(request=request, template_name="endeavorapp/done.html")
