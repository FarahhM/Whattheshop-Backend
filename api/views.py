from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,DestroyAPIView,RetrieveAPIView,CreateAPIView
from .serializers import ListSerializer,DetailSerializer,CreateSerializer, UserCreateSerializer,UserLoginSerializer,ListUserchocieSerializer , UserchocieSerializer 
from .models import Item, Userchocie ,Previoseorders
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class ItemCreateView(CreateAPIView):
    serializer_class = ListSerializer

 
# class OrderCreateView2(CreateAPIView):
#     serializer_class = UserchocieSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)   

class OrderCreateView(APIView):
    serializer_class = ListUserchocieSerializer
    
    def post(self, request):
        order_list = request.data
        order= Previoseorders(user=request.user)
        order.save()

        for x in order_list:
           ItemId  = x['id']
           quantity = x['qty']

           queryset = Item.objects.get(id=ItemId)
           Userchocie.objects.create(item=queryset, quantity=quantity, order=order)
      
     #  userChoice = {
     #     "item": ItemId ,
     #     "qauntity": Quntity ,
     #  }  

     # return  Response(userChoice)
           return Response("success")

class ListPrevioseordersApiView(ListAPIView):
    queryset = Previoseorders.objects.all()
    serializer_class = UserchocieSerializer    
    
class ListApiView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ListSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    permission_classes = [AllowAny]

class ListorderApiView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = UserchocieSerializer


class ListUserchocieApiView(ListAPIView):
    queryset = Userchocie.objects.all()
    serializer_class = ListUserchocieSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    permission_classes = [AllowAny]


class DetailApiView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = DetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'Item'
    permission_classes = [IsAuthenticated]



class UpdateApiView(RetrieveUpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'Item'
    permission_classes = [IsAuthenticated]



class DeleteView(DestroyAPIView):
    queryset = Item.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'Item'
    permission_classes = [IsAuthenticated,IsAdminUser]



class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)



