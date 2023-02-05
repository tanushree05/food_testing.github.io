from django.contrib import admin
from .models import FoodData, FoodItem
from rest_framework_api_key.models import APIKey

api_key, key = APIKey.objects.create_key(name="my-remote-service")
# Register your models here.
admin.site.register(FoodData)
admin.site.register(FoodItem)
from rest_framework.views import APIView
from rest_framework_api_key.models import APIKey
from rest_framework_api_key.permissions import HasAPIKey


class ProjectListView(APIView):
    permission_classes = [HasAPIKey]

    def get(self, request):
        """Retrieve a project based on the request API key."""
        key = request.META["HTTP_AUTHORIZATION"].split()[1]
        api_key = APIKey.objects.get_from_key(key)
        project = Project.objects.get(api_key=api_key)
