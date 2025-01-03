from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from orders.models import Order
from .serializers import OrderCreateSerializer, OrderSerializer

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()  # List all orders
    serializer_class = OrderSerializer 

class OrderCreateView(APIView):
    def post(self, request, *args, **kwargs):
        # Deserialize the data
        serializer = OrderCreateSerializer(data=request.data)

        if serializer.is_valid():
            # Create the order using the serializer
            order = serializer.save()
            return Response(
                {"message": "Order created successfully!", "order_id": order.id},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderCancelView(APIView):
    def post(self, request, *args, **kwargs):
        order_id = request.data.get("order_id")

        try:
            order = Order.objects.get(id=order_id)
            order.cancel_order()

            return Response(
                {"message": "Order canceled successfully!"},
                status=status.HTTP_200_OK
            )

        except Order.DoesNotExist:
            return Response({"error": "Order not found."}, status=status.HTTP_404_NOT_FOUND)
