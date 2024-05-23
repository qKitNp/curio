import time
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from . import curio


# Create your views here.

def index(request):
    return render(request, 'chat/index.html')

class ReplyView(APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        query = request.data.get('query')
        if not query:
            return Response({"error": "query not provided"}, status=status.HTTP_400_BAD_REQUEST)
        message = curio.reply.gemini_response(query)
        time.sleep(2)
        return Response({"message": message}, status=status.HTTP_200_OK)