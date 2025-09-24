from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import RegisterSerializer, MessageSerializer
from .models import Message


# ---------- Registro ----------
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Usuario creado correctamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---------- Login ----------
class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]


# ---------- Enviar mensaje ----------
class SendMessageView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            message = serializer.save(user=request.user)  # Se asocia al usuario autenticado
            return Response(MessageSerializer(message).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---------- Ver progreso ----------
class ProgressView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        messages = Message.objects.filter(user=request.user).order_by("-created_at")
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
