from django.shortcuts import render
from http.client import HTTPResponse
from django.shortcuts import render
from .serializers import FoodDataSerializer
from .models import FoodData, FoodItem
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework_api_key.models import APIKey
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# Create your views here.
class ProjectListView(APIView):
    permission_classes = [HasAPIKey]

    def get(self, request):
        """Retrieve a project based on the request API key."""
        key = request.META["HTTP_AUTHORIZATION"].split()[1]
        api_key = APIKey.objects.get_from_key(key)
        project = Project.objects.get(api_key=api_key)

'''from rest_framework.views import APIView
from rest_framework_api_key.permissions import HasAPIKey

class UserListView(APIView):
    permission_classes = [HasAPIKey & IsAuthenticated]
    '''


def viewOnly(request, pk, format=None):
     if request.method=='GET':
        # GET ALL Ongoing FoodDatas 
        Food = FoodItem.objects.filter(id=pk)
        FoodData_serializer = FoodDataSerializer(Food, many=True)
        return JsonResponse(FoodData_serializer.data, safe=False)
     elif request.method=='POST':
    # THIS CAN BE USED ON ADMIN SITE TO ADD FoodData INFO
        FoodData_data=JSONParser().parse(request)
        FoodData_serializer = FoodDataSerializer(data=FoodData_data)
        if FoodData_serializer.is_valid():
            FoodData_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)

@csrf_exempt
def AdminSide (request,pk, format=None):
      
    if request.method=='POST':
    # THIS CAN BE USED ON ADMIN SITE TO ADD FoodData INFO
        FoodData_data=JSONParser().parse(request)
        FoodData_serializer = FoodDataSerializer(data=FoodData_data)
        if FoodData_serializer.is_valid():
            FoodData_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)

    
    # SELECTING SPECIFIC FoodData BY FoodData BY ID FOR PATCH & DELETE REQUEST
    #     data= JSONParser().parse(request)
    #     FoodData = FoodData.objects.get(id=data.get('id')) 

    elif request.method=='PATCH':
        # UPDATE FoodData INFO
        # SELECTING SPECIFIC FoodData BY FoodData BY ID FOR PATCH & DELETE REQUEST
        data= JSONParser().parse(request)
        object = FoodData.objects.get(id=data.get('id')) 
        FoodData_serializer= FoodDataSerializer(object, data=data, partial=True)
        if FoodData_serializer.is_valid():
            FoodData_serializer.save();
            return JsonResponse("UPDATED", safe=False)

        return JsonResponse("FAILED", safe=False)

    elif request.method=='DELETE':
        # DELETE FoodData INFO
         # SELECTING SPECIFIC FoodData BY FoodData BY ID FOR PATCH & DELETE REQUEST
        data= JSONParser().parse(request)
        Data = FoodData.objects.get(id=pk) 
        Data.delete()
        return JsonResponse("DELETED", safe=False)

