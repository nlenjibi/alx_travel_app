from rest_framework import viewsets
from .models import Listing
from rest_framework import serializers


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'title', 'description']


class ListingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
