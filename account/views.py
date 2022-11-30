import json
import jwt
from django.shortcuts import HttpResponse
from rest_framework import status
from account.models import User, Token
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import ChangePasswordSerializer, RegistrationSerializer , ResetPasswordSerializer
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from Backend.settings import SECRET_KEY
from django.contrib.auth.hashers import check_password
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from Backend.settings import FRONTEND_URL, EMAIL_HOST_USER
from django.core.mail import send_mail
import secrets
from Backend.DecodeToken import decode_token
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from Backend.EmailSend import password_reset_email_send


# Signup view
@api_view(['POST'])
def Signup(request):
    recieved_data = json.loads(request.body)

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=recieved_data)
        renderer_classes = [JSONRenderer]
        if serializer.is_valid():
            user = serializer.save()
            response = f"{user.email} is Successfully created"
            return Response({'data': response})
        else:
            data = serializer.errors
            error = list(data.values())[0]
            print(type(error))
            return Response({'errors': error}, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({'errors': 'Bad Request'})


# custome login view
@api_view(['POST'])
def Signin(request):
    if request.method == 'POST':
        recieved_data = json.loads(request.body)
        email = recieved_data['email']
        password = recieved_data['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active == True:
                login(request, user)
                return Response({'data': "Successfull"})
            else:
                return Response({'data': 'Sorry your account is not active.'})
        else:
            return Response({'error': 'Error'})


# forget password view
@api_view(['POST'])
def ChangePassword(request):
    # forger password code
    if request.method == 'POST':
        recieved_data = json.loads(request.body)
        new_password = recieved_data['new_password']
        password = recieved_data['password']
        serializer = ChangePasswordSerializer(data=recieved_data)
        if serializer.is_valid():
            serializer.validatepassword()
            token = request.headers.get('Authorization')
            decode_token = jwt.decode(
                token.split()[1], SECRET_KEY, algorithms=['HS256'])['user_id']
            user = User.objects.get(id=decode_token)
            correct_password = user.check_password(password)
            print(correct_password)
            if correct_password:
                user.set_password(new_password)
                user.save()
                return Response({'data': 'Password has been changed successfully.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Sorry Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Reset Password
def reset_password(request):
    if request.method == 'POST':
        if not request.headers.get('Authorization'):
            return JsonResponse({"error": "You are unauthorized."}, status=status.HTTP_401_UNAUTHORIZED)
        email_data = json.loads(request.body)
        ValidUser = User.objects.filter(
            email=email_data['email'], is_active=True)
        if ValidUser.exists():
            jwt_token = request.headers.get('Authorization')
            generate_url_safe_token = secrets.token_urlsafe()
            try:
                Istoken_Exist = Token.objects.get(
                    user_id=decode_token(jwt_token))
                return JsonResponse({"data": f"We have already send a reset password email to your provided email id {ValidUser.values()[0]['email']} , Check your email ."}, status=status.HTTP_202_ACCEPTED)
            except ObjectDoesNotExist:
                create_token_model = Token.objects.create(
                    user_id=decode_token(jwt_token), token_value=generate_url_safe_token)
                url = FRONTEND_URL+'/V2/user/reset/password/'+generate_url_safe_token
                # send password reset email
                password_reset_email_send(ValidUser, url)
                return JsonResponse({"data": f"We send a password reset email to your email {ValidUser.values()[0]['email']} ."}, safe=False)
        else:
            return JsonResponse({"error": f"Sorry, The email {email_data['email']} you provide doesn't exist."})
    else:
        return JsonResponse({"error": f"The {request.method} method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



def password_reset_done(request):
    if request.method == 'PUT':
        if not request.headers.get('Authorization'):
            return JsonResponse({"error": "You are unauthorized."}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            jwt_token = request.headers.get('Authorization')
            client_data = json.loads(request.body)
            IstokenValid = Token.objects.get(user_id=decode_token(jwt_token),token_value=client_data['reset_token'])
            serializer = ResetPasswordSerializer(data=client_data)
            if serializer.is_valid():
                serializer.validatepassword()
                user = User.objects.get(id = decode_token(jwt_token))
                user.set_password(client_data['new_password'])
                user.save()
                return JsonResponse({"data":f"The password has been changed successfully."})
            else:
                return JsonResponse({"error"f"{serializer.errors}"})
        except ObjectDoesNotExist:
            return JsonResponse({"error":"Sorry,It seeems like you provided invalid token."},status =status.HTTP_400_BAD_REQUEST)
        
    else:
        return JsonResponse({"error":f"The {request.method} method is not allowed."},status=status.HTTP_405_METHOD_NOT_ALLOWED)
