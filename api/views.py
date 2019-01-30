from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,DestroyAPIView,RetrieveAPIView,CreateAPIView
from .serializers import ListSerializer,DetailSerializer,CreateSerializer, UserCreateSerializer,UserLoginSerializer,ListUserchocieSerializer , UserchocieSerializer 
from .models import Item, Userchocie ,Previoseorders
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response

class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer


class ItemCreateView(CreateAPIView):
	serializer_class = ListSerializer

 


class OrderCreateView(APIView):
	serializer_class = ListUserchocieSerializer
	
	def post(self, request):
		print(request.data)
		order_list = request.data
		order= Previoseorders.objects.create(user=request.user)
		

		for x in order_list:
		   ItemId  = x['id']
		   quantity = x['quantity']
		   size = x["size"]

		   queryset = Item.objects.get(id=ItemId)
		   Userchocie.objects.create(item=queryset, quantity=quantity,size=size ,user=order)
		order.save()
		return Response({"msg":"success"})
	 	# order.save()
	 #  userChoice = {
	 #     "item": ItemId ,
	 #     "qauntity": Quntity ,
	 #  }  

	 # return  Response(userChoice)
		

class ListPrevioseordersApiView(ListAPIView):
	queryset = Previoseorders.objects.all()
	serializer_class = UserchocieSerializer    
	
class ListApiView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ListSerializer
	filter_backends = [SearchFilter,OrderingFilter]
	permission_classes = [AllowAny]

# class ListorderApiView(ListAPIView):
# 	queryset = Item.objects.all()
# 	serializer_class = UserchocieSerializer


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



