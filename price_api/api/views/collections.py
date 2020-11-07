from rest_framework.views import APIView
from rest_framework.response import Response

class Collections(APIView):
    """Class for interacting with the Collections Database."""

    def get(self, request):
        # Get collection from database based on authCode
        # For each card in collection, get price using API I wrote.
        return Response({"Test": "You fetched the collection"})

    def post(self, request):
        return Response()