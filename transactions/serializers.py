from rest_framework import serializers
from .models import Transaction
from django.utils import timezone

class TransactionSerializer(serializers.ModelSerializer):
    PERIOD_FREQUENCY_CHOICES = [
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    ]

    TYPE_FRQUENCY_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    periodicity = serializers.ChoiceField(choices=PERIOD_FREQUENCY_CHOICES)
    type = serializers.ChoiceField(choices=TYPE_FRQUENCY_CHOICES)
    user = serializers.CharField(required=False)

    def create(self, validated_data: dict) -> Transaction:
        transaction = Transaction.objects.create(**validated_data)
        return transaction
    
    def update(self, instance, validated_data):
        instance.updated_at = timezone.now()
        return super().update(instance, validated_data)

    class Meta:
        model = Transaction
        fields = '__all__'