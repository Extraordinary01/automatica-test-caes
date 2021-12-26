from django.urls import path
from .views import TradingPointsListView, VisitCreateView, custom_login

urlpatterns = [
    path('tradingpoints/', TradingPointsListView.as_view()),
    path('login/', custom_login),
    path('visit/create/', VisitCreateView.as_view())
]
