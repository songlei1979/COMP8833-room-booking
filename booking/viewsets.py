from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

from .models import Booking
from .serializers import BookingSerializer
from .permissions import IsBookingOwner


class BookingViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsBookingOwner
    ]

    def get_queryset(self):
        # Anonymous users can view the API,
        # but cannot access any booking records.
        if not self.request.user.is_authenticated:
            return Booking.objects.none()

        # Authenticated users can only see their bookings.
        return Booking.objects.filter(
            user=self.request.user
        )
