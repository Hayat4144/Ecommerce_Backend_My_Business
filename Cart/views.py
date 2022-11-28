
from .models import CartItem, UserCart
from django.http import JsonResponse
from rest_framework.decorators import api_view
import json
from Backend.DecodeToken import decode_token
from account.models import User
from django.db import IntegrityError
from rest_framework import status
from .serialzers import CartItemSerialzer


# Create your views here.


def add_to_cart(request):
    if request.method == "POST":
        cart_data = json.loads(request.body)
        jwt_token = request.headers.get('Authorization')
        UserId = decode_token(jwt_token)
        # check is user valid or not if not throw error
        CheckUserValid = User.objects.filter(id=UserId, is_active=True).values()[0]['id']
        if CheckUserValid is None and len(CheckUserValid) < 1:
            return JsonResponse({"error": "Sorry User can't find."})

        # fetch user cart if not created create it.
        cart, created = UserCart.objects.get_or_create(user_id=CheckUserValid)
        try:
            IsProductExist = CartItem.objects.filter(productItem_id=cart_data['product_item_id'])
            if IsProductExist.exists():
                return JsonResponse({"error": "you have already added this product to your cart."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                Add_Item_to_cart = CartItem.objects.create(
                    cart=cart, productItem_id=cart_data['product_item_id'], quantity=cart_data['quantity'])
            return JsonResponse({"data": f"The {Add_Item_to_cart} has been added Successfully."}, safe=False)
        except IntegrityError:
            pass

    else:
        return JsonResponse({"error": f"{request.method} method is not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


def get_all_cart_item(request):
    jwt_token = request.headers.get('Authorization')
    UserId = decode_token(jwt_token)
    Cart_data = CartItem.objects.filter(cart__user=UserId)
    serializer = CartItemSerialzer(instance=Cart_data,many=True)
    return JsonResponse(serializer.data, safe=False)
