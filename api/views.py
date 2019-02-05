from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,DestroyAPIView,RetrieveAPIView,CreateAPIView

from .serializers import ClassificationSerializer, ListSerializer,DetailSerializer,CartSerializer,CreateSerializer, UserCreateSerializer,UserLoginSerializer,ListUserchocieSerializer , UserchocieSerializer 
from .models import Item, Userchocie ,Previoseorders,Classification

from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class ItemCreateView(CreateAPIView):
    serializer_class = ListSerializer

class ClassificationApiView(ListAPIView):
   queryset = Classification.objects.all()
   serializer_class = ClassificationSerializer


class cartView(APIView):
     
	def post(self, request):
   		   print(request.data)


        order, created = Previoseorders.objects.get_or_create(user=request.user,status=False)
        x = request.data
        

        ItemId  = x['id']
        quantity = x['quantity']
        size = x["size"]
        queryset = Item.objects.get(id=ItemId)
        uc = Userchocie.objects.filter(user=order, item=queryset,size=size)
        if uc:
          uc[0].quantity = uc[0].quantity + 1
          uc[0].save()
        else:
          Userchocie.objects.create(item=queryset, quantity=quantity,size=size ,user=order)


        return Response({"msg":"success"})

            #Userchocie.objects.get(item=id, quantity=quantity,size=size ,user=order)

    def get(self,request):
        order = Previoseorders.objects.get(user=request.user,status=False)
        x = Userchocie.objects.filter(user=order)
        serializer = CartSerializer(x, many=True)
        return Response(serializer.data)

        
class checkoutView(APIView):

    
    def post(self, request):
        order = Previoseorders.objects.get(user=request.user,status=False)
        order.status = True
        order.save()

        return Response({"msg":"success"})
       



# class OrderCreateView(APIView):
#   #serializer_class = ListUserchocieSerializer
    
#   def post(self, request):
#       print(request.data)
#       order_list = request.data
#       order= Previoseorders.objects.create(user=request.user)
        
#       for x in order_list:
#          ItemId  = x['id']
#          quantity = x['quantity']
#          size = x["size"]

#          queryset = Item.objects.get(id=ItemId)
#          Userchocie.objects.create(item=queryset, quantity=quantity,size=size ,user=order)
#       order.save()
#       return Response({"msg":"success"})
    
        

class ListPrevioseordersApiView(ListAPIView):
    #queryset = Previoseorders.objects.all()
    serializer_class = UserchocieSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Previoseorders.objects.filter(user=user)
        # return user.accounts.all()

class ListallPrevioseordersApiView(ListAPIView):
    queryset = Previoseorders.objects.all()
    serializer_class = UserchocieSerializer
    
		


class ListApiView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ListSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    permission_classes = [AllowAny]

class ListmenApiView(ListAPIView):
  
    serializer_class = ListSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    permission_classes = [AllowAny]
    def get_queryset(self):
        user = self.request.user
        return Item.objects.filter(gender="Men")
        # return user.accounts.all()
class ListKidsApiView(ListAPIView):
  
    serializer_class = ListSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    permission_classes = [AllowAny]
    def get_queryset(self):
        user = self.request.user
        return Item.objects.filter(gender="Kids")

class ListWomenApiView(ListAPIView):
  
    serializer_class = ListSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    permission_classes = [AllowAny]
    def get_queryset(self):
        user = self.request.user
        return Item.objects.filter(gender="Women")


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



