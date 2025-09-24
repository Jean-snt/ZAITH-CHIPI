from django.urls import path
from .views import RegisterView, LoginView, SendMessageView, ProgressView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('send-message/', SendMessageView.as_view(), name="send_message"),
    path('progress/', ProgressView.as_view(), name="progress"),
]
