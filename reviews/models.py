from django.db import models
from django.conf import settings


class Ticket(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tickets')
	title = models.CharField(max_length=128)
	description = models.TextField()


class Review(models.Model):
	ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='reviews')
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
	rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(6)])
	headline = models.CharField(max_length=128)
	body = models.TextField(blank=True)


class UserFollows(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
	followed_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by')

	class Meta:
		unique_together = ('user', 'followed_user')

