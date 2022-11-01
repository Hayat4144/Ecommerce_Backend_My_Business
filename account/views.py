import json
import jwt
from django.shortcuts import HttpResponse
from rest_framework import status
from account.models import User
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import ForgetPasswordSerializer, RegistrationSerializer
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate ,login
from Backend.settings import SECRET_KEY
from django.contrib.auth.hashers import check_password
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView 

# Signup view
@api_view(['POST'])
def Signup(request):
    recieved_data = json.loads(request.body)

    if request.method == 'POST':
        serializer = RegistrationSerializer(data = recieved_data)
        renderer_classes = [JSONRenderer]
        if serializer.is_valid():
            user = serializer.save()
            response = f"{user.email} is Successfully created"
            return Response({'data':response})
        else:
            data = serializer.errors
            error = list(data.values())[0]
            print(type(error))               
            return Response({'errors':error},status=status.HTTP_400_BAD_REQUEST)
        
    else:
        return Response({'errors':'Bad Request'})
        
    

# custome login view
@api_view(['POST'])
def Signin(request):
    if request.method == 'POST':
        recieved_data = json.loads(request.body)
        email = recieved_data['email']
        password = recieved_data['password']
        user = authenticate(username =email, password = password)
        if user is not None:
            if user.is_active == True:
                login(request,user)
                return Response({'data':"Successfull"})
            else:
                return Response({'data':'Sorry your account is not active.'})
        else:
            return Response({'error':'Error'})




# forget password view
@api_view(['POST'])
def ForgetPassword(request):
    # forger password code 
    if request.method == 'POST':
        recieved_data = json.loads(request.body)
        new_password = recieved_data['new_password']
        old_password = recieved_data['password']
        serializer = ForgetPasswordSerializer(data =recieved_data)
        if serializer.is_valid():
            serializer.validatepassword()
            token = request.headers.get('Authorization')
            decode_token = jwt.decode(token.split()[1],SECRET_KEY,algorithms=['HS256'])['user_id']
            user  = User.objects.get(id=decode_token)
            correct_password = user.check_password(old_password)
            print(correct_password)
            if correct_password:
                user.set_password(new_password)
                user.save()
                return Response({'data':'password has been changed successfully.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error':'Sorry Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
