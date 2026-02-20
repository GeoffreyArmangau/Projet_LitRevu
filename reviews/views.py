from .models import Ticket
from .forms_review import ReviewForm
from django.shortcuts import get_object_or_404

from django.utils.html import format_html

from django.urls import reverse

from django.contrib.auth.decorators import login_required

@login_required
def create_review_answer(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    # Affichage HTML du ticket (simple, à personnaliser si besoin)
    ticket_display = format_html(
        '<div class="ticket-display">'
        '<strong>{}</strong><br>'
        '{}<br>'
        '{}'
        '</div>',
        ticket.title,
        ticket.description,
        (f'<img src="{ticket.image.url}" alt="Image du ticket" style="max-width:180px;max-height:180px;">' if ticket.image else '')
    )
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('flux')
    else:
        review_form = ReviewForm()
    return render(request, 'reviews/create_review_answer.html', {
        'review_form': review_form,
        'ticket_display': ticket_display,
        'ticket': ticket,
    })
from .forms_review import ReviewForm

from .forms_review import ReviewForm

from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

@login_required
def create_review(request):
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        if ticket_form.is_valid() and review_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('flux')
    else:
        ticket_form = TicketForm()
        review_form = ReviewForm()
    return render(request, 'reviews/create_review.html', {'ticket_form': ticket_form, 'review_form': review_form})
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth import get_user_model
from .models import Review, Ticket
from .forms import TicketForm

from django.shortcuts import redirect

@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('flux')
    else:
        form = TicketForm()
    return render(request, 'reviews/create_ticket.html', {'form': form})

@login_required
def flux(request):
    return render(request, "flux.html")

@login_required
def flux_data(request):
    # Exemple de récupération de données, à adapter selon tes modèles
    user = request.user
    # Critiques de l'utilisateur
    my_reviews = Review.objects.filter(user=user)
    # Critiques des abonnements (à adapter selon ton modèle d'abonnement)
    # reviews_from_followed = ...
    # Billets à critiquer (à adapter selon ton modèle de ticket)
    # tickets_to_review = ...
    # Pour la démo, on ne renvoie que les critiques de l'utilisateur
    data = []
    for review in my_reviews:
        data.append({
            'type': 'Ma critique',
            'author': review.user.username,
            'content': review.content,
            'date': review.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        })
    # À compléter avec les autres types d'éléments
    # data.extend(...)
    # Tri par date décroissante
    data.sort(key=lambda x: x['date'], reverse=True)
    return JsonResponse({'flux': data})
