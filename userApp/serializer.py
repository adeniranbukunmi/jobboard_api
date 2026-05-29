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
  
    def update(self, instance, validated_data):
        user = self.context['request'].user
        if instance != user:
            raise serializers.ValidationError("You can only update your own account.")
        password = validated_data.pop("password", None)
        if password is not None:
            instance.set_password(password)
            instance.save()
        return super().update(instance, validated_data)
