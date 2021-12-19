from dataclasses import fields
from rest_framework import serializers
from accounts.models import MyUser, MyUserLoc, UserHistory
from stores.models import Store, StoreItems
from boards.models import Boards, Advetiesments

from django.contrib.auth import authenticate, models


class MyUserRegistrationSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(
                style={'input_type' : 'password'}, write_only =True
    ) 
    
    class Meta:
        model = MyUser
        fields = (
            'username','email','first_name','last_name','password','password2', 'date_of_birth',
        )
        extra_kwargs = {
            'password' : {'write_only': True}
        }
    
    def save(self):
        account = MyUser(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            date_of_birth = self.validated_data['date_of_birth']
        )
        
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'password':'passwords not match'})
        account.set_password(password)
        account.save()

class StoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id',
                  'name',
                  'lat',
                  'lon',
                  'store_type',
                  'image',
        )

class StoreItemsSerializer(serializers.ModelSerializer):
    # image_url = serializers.SerializerMethodField()
    class Meta:
        model = StoreItems
        fields = (
            'id',
            'store',
            'name' ,
            'discription',
            'discount' ,
            'price',
            'No_of_items',
            'item_image',
        )
    # def get_image_url(self,storeItem):
    #     request = self.context.get('request')

class MyUserLocSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUserLoc
        fields = (
            # 'id',
            'user',
            # 'user_id',
            # 'username',
            'lat',
            'lon',
        )

class UserHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHistory
        fields = (
            "user",
            "search_item_name",
        )
            
class BoardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boards
        fields = (
            'id',
            'lon',
            'lat'
        )
        
        
class AdvetiesmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advetiesments
        fields = (
            'name',
            'adv_type',
            'image'
        )