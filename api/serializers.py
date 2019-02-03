from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Item , Userchoice ,Previoseorders


class ListUserchoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userchoice
        fields = ["item","quantity","size"]



class UserchoiceSerializer(serializers.ModelSerializer):
    choice = serializers.SerializerMethodField()
    totalprice = serializers.SerializerMethodField()
    class Meta:
        model = Previoseorders
        fields = ["id","user", "choice" , "date" , "totalprice"]

    def get_choice(self,obj):
        return ListUserchoiceSerializer(obj.userchoice_set,many=True).data
    def get_totalprice(self,obj):
        return obj.total()

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password' , 'email' ,'first_name','last_name']

    def create(self, validated_data):
        email = validated_data['email']
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        new_user = User(username=username,email=email,first_name=first_name,last_name=last_name)
        new_user.set_password(password)
        new_user.save()
        return validated_data

class UserLoginSerializer(serializers.Serializer):   
    def validate(self, data):
        my_username = data.get('username')
        my_password = data.get('password')

        try:
            user_obj = User.objects.get(username=my_username)
        except:
            raise serializers.ValidationError("This username does not exist")

        if not user_obj.check_password(my_password):
            raise serializers.ValidationError("Incorrect username/password combination! ")

        return data


