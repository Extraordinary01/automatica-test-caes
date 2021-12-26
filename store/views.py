from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_201_CREATED, HTTP_200_OK
from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, serializers

from .models import TradingPoint
from .serializers import TradingPointSerializer, VisitSerializer

@api_view(['POST'])
def custom_login(request):
    data = request.data
    try:
        phone = data['phone']
        password = data['password']
    except:
        return Response(status=HTTP_400_BAD_REQUEST)
    user = authenticate(phone=phone, password=password)
    if user is None:
        return Response(status=HTTP_401_UNAUTHORIZED)

    token, created = Token.objects.get_or_create(user=user)
    return Response(data={ 'token': token.key }, status=HTTP_200_OK)


class TradingPointsListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TradingPointSerializer

    def get_queryset(self):
        print(self.request.user)
        qs = TradingPoint.objects.filter(employee=self.request.user)
        return qs

class VisitCreateView(generics.CreateAPIView):
    serializer_class = VisitSerializer

