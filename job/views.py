from django.contrib.auth import authenticate
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from drf_spectacular.utils import extend_schema
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from job.models import Job

from .serializers import JobSerializer, LoginSerializer


def home(request: HttpRequest):
    context = {"title":"Home Page", "data":"Some randoom data"}
    return render(request, "index.html", context)

class AboutView(TemplateView):
    template_name = "about.html"


class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    
    @extend_schema(
        request=LoginSerializer,)
    def post(self, request: Request):
        """Login with email and password"""
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            email=serializer.validated_data["email"], 
            password=serializer.validated_data["password"]
        )
        if not user:
            return Response({"error": "Invalid credentials"}, status=400)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class JobListView(APIView):
    """
    List all jobs.
    """
    @extend_schema(responses=JobSerializer(many=True))
    def get(self, request, format=None):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)



