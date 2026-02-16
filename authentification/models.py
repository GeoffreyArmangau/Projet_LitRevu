from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	# Ajoutez ici d'autres champs personnalisés si besoin (bio, avatar, etc.)
	pass
