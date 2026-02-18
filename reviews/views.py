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
