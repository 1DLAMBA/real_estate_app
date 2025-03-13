from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import NextOfKin

User = get_user_model()

class NextOfKinSerializer(serializers.ModelSerializer):
    class Meta:
        model = NextOfKin
        fields = ['id', 'name', 'relationship', 'phone_number', 'occupation']

class UserSerializer(serializers.ModelSerializer):
    next_of_kin = NextOfKinSerializer(required=False)
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 
                  'user_type', 'gender', 'date_of_birth', 'nationality', 'phone_number', 
                  'address', 'delivery_address', 'profile_rank', 'next_of_kin']
        read_only_fields = ['profile_rank']
    
    def create(self, validated_data):
        next_of_kin_data = validated_data.pop('next_of_kin', None)
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        
        if next_of_kin_data:
            NextOfKin.objects.create(user=user, **next_of_kin_data)
        
        return user
    
    def update(self, instance, validated_data):
        next_of_kin_data = validated_data.pop('next_of_kin', None)
        password = validated_data.pop('password', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
            
        if password:
            instance.set_password(password)
        
        instance.save()
        
        if next_of_kin_data:
            next_of_kin, created = NextOfKin.objects.get_or_create(user=instance)
            for attr, value in next_of_kin_data.items():
                setattr(next_of_kin, attr, value)
            next_of_kin.save()
            
        return instance