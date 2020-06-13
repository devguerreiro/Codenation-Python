from django.db import models


class Event(models.Model):
    LEVELS_CHOICES = [
        ("CRITICAL", "Critical"),
        ("DEBUG", "Debug"),
        ("ERROR", "Error"),
        ("INFO", "Info"),
        ("WARNING", "Warning"),
    ]

    level = models.CharField(max_length=20, choices=LEVELS_CHOICES)
    data = models.TextField()
    agent = models.ForeignKey("Agent", related_name="events", on_delete=models.CASCADE)
    user = models.ForeignKey("User", related_name="events", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    arquivado = models.BooleanField(default=False)
