from django.utils import timezone
from reviews.models import Ticket, Review

now = timezone.now()

Ticket.objects.filter(created_at__isnull=True).update(created_at=now)
Ticket.objects.filter(updated_at__isnull=True).update(updated_at=now)
Review.objects.filter(created_at__isnull=True).update(created_at=now)
Review.objects.filter(updated_at__isnull=True).update(updated_at=now)
print('Champs NULL corrigés.')
