from rest_framework import viewsets
from task.models import Category
from task.serializers import CategorySerializer

# Create your views here.
class CategoreViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer