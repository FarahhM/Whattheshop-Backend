from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,DestroyAPIView,RetrieveAPIView,CreateAPIView
from .serializers import ListSerializer,DetailSerializer,CreateSerializer,UserCreateSerializer,UserLoginSerializer
from .models import Shop
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class ListApiView(ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ListSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['username', 'password']
    permission_classes = [AllowAny]



class DetailApiView(RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = DetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'shop'
    permission_classes = [IsAuthenticated]



class UpdateApiView(RetrieveUpdateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'shop'
    permission_classes = [IsAuthenticated]



class DeleteView(DestroyAPIView):
    queryset = Shop.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'shop'
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

