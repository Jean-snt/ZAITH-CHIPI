from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    original_text = models.TextField()
    corrected_text = models.TextField(blank=True, null=True)  # lo agrega la IA
    feedback = models.TextField(blank=True, null=True)        # explicación de la IA
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.user.username} en {self.created_at}"
