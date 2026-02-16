from django.db import models
from django.conf import settings


class Ticket(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tickets')
	title = models.CharField(max_length=128)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.title} ({self.user})"

class Review(models.Model):
	ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='reviews')
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
	rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(6)])
	headline = models.CharField(max_length=128)
	body = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.headline} ({self.user})"

class UserFollows(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
	followed_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by')
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ('user', 'followed_user')

	def __str__(self):
		return f"{self.user} suit {self.followed_user}"
