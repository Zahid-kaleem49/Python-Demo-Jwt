from django.http import HttpResponse
from .models import CartItem
from .serializers import CartItemSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator
from .serializers import UserModelSerializer
from django.contrib.auth.hashers import make_password

# Create your views here.


@permission_classes([IsAuthenticated])
class CartItemList (ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    
    
@permission_classes([IsAuthenticated])
class CartItemViews(APIView):
    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, id=None):
        try:
            if id:
                item = CartItem.objects.get(id=id)
                serializer = CartItemSerializer(item)
                json_data = JSONRenderer().render(serializer.data)
                # return HttpResponse(json_data, content_type = 'application/json')
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                items = CartItem.objects.all()
                serializer = CartItemSerializer(items, many=True)
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({"status": "failed", "data": "no data found"}, status=status.HTTP_404_NOT_FOUND)
    
    def patch (self, request, id=None):
        item = CartItem.objects.get(id=id)
        serializer = CartItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status" : "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id=None):
        item =get_object_or_404(CartItem, id=id)
        item.delete()
        return Response({"status": "success", "data":"item deleted"})
    

class CreateUser(APIView):
    def post(self, request):            
        serializer_class = UserModelSerializer(data=request.data)
        if serializer_class.is_valid():
            password = serializer_class.validated_data.get('password')
            serializer_class.validated_data['password'] = make_password(
                password)
            serializer_class.save()
            return Response({'message': 'User Registered'}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {'message': 'User Not Registered',
                    "Error": serializer_class.errors},
                status=status.HTTP_400_BAD_REQUEST
            )


class Testtest(APIView):
    def get(self, request):
        return Response({'message': 'User Not Registered'})
