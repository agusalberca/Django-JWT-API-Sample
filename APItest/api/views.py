from django.shortcuts import render
from .models import Wallet,Transaction
from .serializers import WalletSerializer, TransactionSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

class HelloView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [ permissions.IsAuthenticated ]
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class RegisterWallet(CreateAPIView):
    model = Wallet
    authentication_classes = [JWTAuthentication]
    permission_classes = [ permissions.IsAuthenticated ]
    serializer_class = WalletSerializer

class RetrieveUpdateDestroyWallet(RetrieveUpdateDestroyAPIView):
    model = Wallet
    queryset = Wallet.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [ permissions.IsAuthenticated ]
    serializer_class = WalletSerializer

    
# class RegisterTransaction(CreateAPIView):
#     model = Transaction
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [ permissions.IsAuthenticated ]
#     serializer_class = TransactionSerializer    

# class RetrieveUpdateDestroyTransaction(RetrieveUpdateDestroyAPIView):
#     model = Transaction
#     queryset = Transaction.objects.all()
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [ permissions.IsAuthenticated ]
#     serializer_class = TransactionSerializer
#TODO finish implementation

