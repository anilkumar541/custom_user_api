from django.shortcuts import render, HttpResponse

# Create your views here.
from rest_framework.generics import CreateAPIView
from accounts.serializers import CustomUserSerializer
from accounts.models import CustomUser
from django.core.mail import send_mail
from django.conf import settings


class CreateUser(CreateAPIView):
  
    queryset=CustomUser.objects.all()
    serializer_class=CustomUserSerializer

    def post(self, request):
        username = request.POST["username"]
        email = request.POST["email"]

        subject="welcome to the oscorp"
        message=f"congrats {username} you have successfully registered"
        from_email=settings.EMAIL_HOST_USER
        recepient_list=[email]


        send_mail(subject, message, from_email, recepient_list, fail_silently=False)
        return HttpResponse("check you email gentle man")


