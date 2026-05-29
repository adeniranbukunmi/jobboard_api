from rest_framework import serializers
from userApp.models import CustomUserAcct




class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUserAcct
        fields=["id","first_name", "last_name", "email", "password","phone_num","address","user_type"]
        
        extra_kwargs={"id":{"read_only":True}, "password":{"write_only":True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = super().create(validated_data)
        if password is not None:
            user.set_password(password)
            user.save()
  
