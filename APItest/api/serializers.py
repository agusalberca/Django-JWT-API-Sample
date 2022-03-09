from rest_framework import serializers
from .models import Wallet,Transaction

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['dir', 'balance']
        
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['date', 'amount', 'from_wallet', 'to_wallet']