from .serializers import CustomerSerializer
from customers.models import Customer
import names
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from random import randrange
from datetime import timedelta, datetime


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


# siege -c 60 -t 600s --content-type="application/json" 'http://localhost:8000/customers/create/ POST'
class CustomerCreateAPIView(APIView):

    def post(self, request, *args, **kwargs):
        Customer.objects.create(
            name=names.get_full_name(),
            birthday=random_date(datetime(1980, 1, 1).date(), datetime.now().date())
        )

        return Response({"status": "OK"}, status=status.HTTP_201_CREATED)


class CustomerReceiveAPIView(RetrieveAPIView):
    serializer_class = CustomerSerializer

    def get_object(self):
        customer = Customer.objects.filter(id=self.kwargs.get("customer_id")).first()
        if customer is not None:
            return customer
        raise NotFound()


class CustomerListAPIView(ListAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
