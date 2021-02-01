from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import UserSerializer, GroupSerializer, ItemSerializer, UserRegistrationSerializer, \
    CharityRegistrationSerializer, UserLoginSerializer, CharityGetAllSerializer, OrderItemSerializer
from .models import CharityRegistration, UserRegistration, Item
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_item(request):
    serializer = ItemSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"Status": "Added"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register_new_charity(request):
    serializer = CharityRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Status": "Added"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_new_charity(request):
    serializer = CharityRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.data['email']
        try:
            password = list(CharityRegistration.objects.filter(email=email).values())[0]['password']
            print(password)
            if password == serializer.data['password']:
                return Response({"Status": "Success"}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"Status": "Fail"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"Status": "User Not Found"}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.data['email']
        try:
            password = list(UserRegistration.objects.filter(email=email).values())[0]['password']
            print(password)
            if password == serializer.data['password']:
                return Response({"Status": "Success"}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"Status": "Fail"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"Status": "User Not Found"}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_charities(request):
    charities = CharityRegistration.objects.all().order_by('-charity_name')
    serializer = CharityGetAllSerializer(charities, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_items_by_charity(request):
    email = dict(request.data)['email'][0]
    charities = Item.objects.filter(charity=email)
    serializer = ItemSerializer(charities, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def order_new_item(request):
    serializer = OrderItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Status": "Ordered"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def modify_charity_details(request):
    serializer = CharityRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.data['email']
        charity_name = serializer.data['charity_name']
        password = serializer.data['password']
        city = serializer.data['city']
        CharityRegistration.objects.filter(email=email).update(charity_name=charity_name, password=password, city=city)
        return Response({"Status": "Modified"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_charity_participants(request):
    charity_name = dict(request.data)['charity_name'][0]
    participants = UserRegistration.objects.filter(charity_name=charity_name)
    serializer = UserRegistrationSerializer(participants, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_item(request):
    itemId = dict(request.data)['itemID'][0]
    Item.objects.get(itemID=itemId).delete()

    return Response({"Status": "Deleted"}, status=status.HTTP_200_OK)
