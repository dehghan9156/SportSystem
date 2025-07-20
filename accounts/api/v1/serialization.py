from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields =["name","family","role","username","password","confirm_password"]
        write_only_fields =["confirm_password"]

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("password and confirmpassword does not match.")
        return data
    
    def create(self,validated_data):
        validated_data.pop("confirm_password")
        user = User.objects.create_user(**validated_data)
        return user