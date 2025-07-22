from rest_framework import serializers
from ...models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]
        
class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = ["title","start_date","end_date","longitude","latitude","category"]