from .models import UserWhishlist, WhishlistItem
from django.http import JsonResponse
from rest_framework.decorators import api_view
import json
from Backend.DecodeToken import decode_token
from account.models import User
from django.db import IntegrityError
from rest_framework import status
from .serailzers import WhishlistItemSerialzer


# add to whishlist
def add_to_whishlist(request):
    if request.method == "POST":
        whishlist_data = json.loads(request.body)
        jwt_token = request.headers.get('Authorization')
        UserId = decode_token(jwt_token)
        # check is user valid or not if not throw error
        CheckUserValid = User.objects.filter(
            id=UserId, is_active=True).values()[0]['id']
        if CheckUserValid is None and len(CheckUserValid) < 1:
            return JsonResponse({"error": "Sorry User can't find."})

        whishlist, created = UserWhishlist.objects.get_or_create(
            user_id=CheckUserValid)
        try:
            IsProductExist = WhishlistItem.objects.filter(
                productItem_id=whishlist_data['product_item_id'])
            if IsProductExist.exists():
                return JsonResponse({"error": "you have already added this product to your cart."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                Add_Item_to_whishlist = WhishlistItem.objects.create(
                    whishlist=whishlist, productItem_id=whishlist_data['product_item_id'])
            return JsonResponse({"data": f"The {Add_Item_to_whishlist} has been added Successfully."}, safe=False)
        except IntegrityError:
            pass

        JsonResponse('htlkjdsf', safe=False)
    else:
        return JsonResponse({"error": f"{request.method} method is not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)




# get wishlistItem of specific user only
def get_all_wishlistItem(request):
    if request.method == 'GET':
        if not request.headers.get('Authorization'):
            return JsonResponse({"error": "You are unauthorized."}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            jwt_token = request.headers.get('Authorization')
            UserId = decode_token(jwt_token)
            Wishlist_data = WhishlistItem.objects.filter(
                whishlist__user=UserId)
            serializer = WhishlistItemSerialzer(
                instance=Wishlist_data, many=True)
            return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({"error": f"The {request.method} method is not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# delete whishlistItem
def delete_wishlistItem(request):
    if request.method == 'DELETE':
        if not request.headers.get('Authorization'):
            return JsonResponse({"error": "You are unauthorized."}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            jwt_token = request.headers.get('Authorization')
            WhishlistItemId = json.loads(request.body)
            if WhishlistItem.objects.filter(id=WhishlistItemId['whishlist_id']).exists():
                UserId = decode_token(jwt_token)
                delete_cartItem = WhishlistItem.objects.filter(
                    whishlist__user=UserId, id=WhishlistItemId['whishlist_id'])
                delete_cartItem.delete()
                return JsonResponse({"data": "The Whishlist item has been deleted."}, safe=False)
            else:
                return JsonResponse({"error": "The Whishlist doesn't exist."}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({"error": f"The {request.method} method is not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
