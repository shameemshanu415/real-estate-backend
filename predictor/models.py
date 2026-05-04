from django.db import models
from django.contrib.auth.models import User


# 🔮 Prediction History
class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    area = models.FloatField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField(default=0)
    floors = models.IntegerField(default=0)
    year_built = models.IntegerField(null=True, blank=True)
    condition = models.CharField(max_length=50, blank=True, null=True)
    garage = models.BooleanField(default=False)
    location = models.CharField(max_length=50, blank=True, null=True)
    property_type = models.CharField(max_length=50, blank=True, null=True)
    predicted_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


# 🤖 Chat History
class ChatHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)