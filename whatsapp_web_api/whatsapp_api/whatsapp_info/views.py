from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import info_serializers
from .models import WhatsappInfo

# Create your views here.
@api_view(['GET'])
def apiview(request):
    api_urls = {
        'Name':'/Name/',
        'phone_number':'/phone_number/',

    }
    return Response(api_urls)

@api_view(['POST'])
def Create_Api_1(request):
    serializer = info_serializers(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def showall(request):
    info = WhatsappInfo.objects.all()
    serializer = info_serializers(info, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def show_phone_number(request,pk):
#     info = WhatsappInfo.objects.get(id=pk)
#     serializer = info_serializers(info ,many= False)
#     # if serializer.is_valid():
#     #     serializer.save()
#     return Response(serializer.data)










