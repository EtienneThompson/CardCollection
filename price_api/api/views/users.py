from rest_framework.response import Response
from rest_framework.views import APIView


class Users(APIView):
    """Class for interacting with the Users database."""

    def get(self, request):
        return Response({"test": "You fetched the user"})

    def post(self, request):
        return Response()
