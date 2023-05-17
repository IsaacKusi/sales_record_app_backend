
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import SaleItemserializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from recordapp.models import SaleItem
from rest_framework.permissions import IsAuthenticated

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class GetSalesSerializer(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, user_id):
        qs = SaleItem.objects.filter(user_id = user_id)
        serializer= SaleItemserializer(qs, many=True)
        return Response(serializer.data)


class SaleItemSerializerView(APIView):    
    def post(self, request, *args, **kwargs):
        serializer = SaleItemserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class SaleItemsDelete(APIView):
    def delete (self, request, item_id,user_id):
      try:  
        item = SaleItem.objects.get(item_id = item_id, user_id = user_id)
      except SaleItem.DoesNotExist:
          return Response({'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
      item.delete()
      return Response({'message':'sale record succesfully deleted'})



