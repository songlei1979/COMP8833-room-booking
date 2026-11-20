from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.authentication import TokenAuthentication

from .models import Booking
from .serializers import BookingSerializer
from .permissions import IsBookingOwner


from .models import Room
from .serializers import RoomSerializer


class RoomViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [AllowAny]

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, IsBookingOwner]

    def get_queryset(self):
        return Booking.objects.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)