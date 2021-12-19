from typing import ItemsView
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import auth
from django.shortcuts import HttpResponse

from accounts.models import MyUserLoc, UserHistory, MyUser
# from stores.documents import StoreItemsDoc

from.serializers import ( 
                         MyUserLocSerializer, MyUserRegistrationSerializer, 
                         StoresSerializer, 
                         StoreItemsSerializer, UserHistorySerializer, 
                         BoardsSerializer, AdvetiesmentsSerializer
                        )

from stores.models import Store, StoreItems
from boards.models import Boards, Advetiesments

import base64
from io import BytesIO
from PIL import Image

# from django_elasticsearch_dsl_drf.filter_backends import (
#     FilteringFilterBackend,
#     CompoundSearchFilterBackend
# )
# from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
# from django_elasticsearch_dsl_drf.filter_backends import (
#     FilteringFilterBackend,
#     OrderingFilterBackend,
# )


def location_default(data):
    serializer = MyUserLocSerializer(data=data)
    user_det = MyUser.objects.get(id=data["user"])
    
    if user_det:
        print("user_Det",user_det)
        pass
    if serializer.is_valid():
        serializer.save()
        
@api_view(['POST'])
def registration_view(request):
    data={}
    if request.method == 'POST':
        serializer = MyUserRegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully registered a new user"
        else:
            data = serializer.errors
            
    return Response(data)   

def login(request):
    if request.method == 'GET':
        username = request.GET['username']
        password = request.GET['user_pass']
        
        user = auth.authenticate(username=username, password=password)
        data = {}
        if user is not None:
            auth.login(request, user)
            data['response'] = 'OK'
            data1 = MyUser.objects.filter(email = user)
            location_default({
                "user":data1.values('id')[0]['id'],
                "lat": 0,
                "lon":0
            })
            return HttpResponse({data1.values('id')[0]['id']})
            
        else:
            data['response'] = 'invalid'
            return HttpResponse({"invalid"})
    
    return HttpResponse({"enter data"})

@api_view(['GET'])
def getStores(request):
    items = Store.objects.all()
    serializer = StoresSerializer(items, many=True)
    # items_dic = {}
    # item_count = 0
    # for item in serializer.data:
    #     image = Image.open(item['image'][1:])
    #     buffered = BytesIO()
    #     image.save(buffered, format="JPEG")
    #     img_str = base64.b64encode(buffered.getvalue())

    #     data = {"img_data": img_str}
    #     data.update(dict(item))
    
    #     items_dic[item_count] = dict(data)
    #     item_count +=1
    
    # return Response(items_dic)
    return Response(serializer.data)

@api_view(['GET'])
def getStoreItems(request):
    items = StoreItems.objects.all()
    serializer = StoreItemsSerializer(items, many=True)
    # items_dic = {}
    # item_count = 0
    # for item in serializer.data:
    #     image = Image.open(item['item_image'][1:])
    #     buffered = BytesIO()
    #     image.save(buffered, format="JPEG")
    #     img_str = base64.b64encode(buffered.getvalue())

    #     data = {"img_data": img_str}
    #     data.update(dict(item))
        
    #     items_dic[str(item_count)] = dict(data)
    #     item_count +=1
    return Response(serializer.data)

@api_view(['GET'])
def getStore(request,pk):
    items = Store.objects.get(id=pk)
    serializer = StoresSerializer(items, many=False)

    # image = Image.open(serializer.data['image'][1:])
    # buffered = BytesIO()
    # image.save(buffered, format="JPEG")
    # img_str = base64.b64encode(buffered.getvalue())

    # data = {"img_data": img_str}
    # data.update(dict(serializer.data))
    
    return Response(serializer.data)

@api_view(['GET'])
def getStoreItem(request,pk):
    items = StoreItems.objects.get(id=pk)
    serializer = StoreItemsSerializer(items, many=False)

    # image = Image.open(serializer.data['item_image'][1:])
    # buffered = BytesIO()
    # image.save(buffered, format="JPEG")
    # img_str = base64.b64encode(buffered.getvalue())

    # data = {"img_data": img_str}
    # data.update(dict(serializer.data))
    
    return Response(serializer.data)

@api_view(['POST'])
def userLocUpdate(request,pk):
    items = MyUserLoc.objects.get(user=pk)
    serializer = MyUserLocSerializer(instance=items, data=request.data)
    
    if serializer.is_valid(): 
        serializer.save()
        print('is valid')
    else:
        print('not valid')
    return Response(serializer.data)


@api_view(['GET'])
def getuserLoc(request,pk):
    items = MyUserLoc.objects.get(user=pk)
    serializer = MyUserLocSerializer(items, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getuserHistory(request,pk):
    items = UserHistory.objects.get(user=pk)
    serializer = UserHistorySerializer(items, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getusersHistory(request):
    items = UserHistory.objects.all()
    serializer = UserHistorySerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getusersLoc(request):
    items = MyUserLoc.objects.all()
    serializer = MyUserLocSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getboardlocs(request):
    locs = Boards.objects.all()
    serializer = BoardsSerializer(locs, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def userHistory(request):
    serializer = UserHistorySerializer(data=request.data)
    if serializer.is_valid(): 
        serializer.save()
        print('is valid')
    else:
        print('not valid')
    return Response(serializer.data)

@api_view(['GET'])
def getboardAdv(request):
    items = Advetiesments.objects.all()
    serializer = AdvetiesmentsSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'stores             ': '/stores/',
        'store Items        ': '/storeItems/',
        # 'Create'          : '/project-data-create/',
        'store              ': 'store/<str:pk>/',
        'store Item         ': 'storeItem/<str:pk>',

        'user Loc Update     ': 'userLocUpdate/<str:pk>/',
        'get User Loc        ': 'getuserLoc/<str:pk>/',
        'get users Loc       ': 'getusersLoc/',

        # 'userHistory'       :'userHistory/<str:pk>/'
        'user History        ': 'userHistory/',
        'getusersHistory     ': 'getusersHistory/',
        'getuserHistory      ': 'getuserHistory/',

        # 'search              ': 'search/?search=<str>',
        
        'boardlocs           ': 'boardlocs/',
        'getboardAdv         ': 'getboardAdv/'
    }
    return Response(api_urls)

# class PublisherDocumentView(DocumentViewSet):
#     document = StoreItemsDoc
#     serializer_class = StoreItemsDocSerializer
#     lookup_field = 'name'
#     fielddata=True
#     filter_backends = [
#         FilteringFilterBackend,
#         OrderingFilterBackend,
#         CompoundSearchFilterBackend,
#     ]
   
#     search_fields = (
#         'name',
#         'discription',
#     )
#     multi_match_search_fields = (
#        'name',
#         'discription',
#     )
#     filter_fields = {
#        'name' : 'name',
#         'discription' : 'discription',
#     }
#     ordering_fields = {
#         'id': None,
#     }
#     ordering = ( 'id'  ,)
    
    
