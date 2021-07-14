from rest_framework.views  import APIView
from rest_framework.response import Response

from rest_framework import status
from profiles_api import serializers



class HelloApiView(APIView):
    """Test APIView"""

    serializer_class=serializers.HelloSerializer

    def get(self, request,format=None):
        """return a list of APIView features"""
        an_apiview = [
            "USes HTTP methods as function (get, post, put, delete)",
            "IS similar to a traditional DJango view",
            "Gives you teh most control over your application logic",
            "is mapped manually to URLs" ,
        ]
        return Response({"message":"hello", "an_apiview":an_apiview})

    def post(self, request):
        """Create an hello message with our name"""
        serializer =self.serializer_class(data=request.data)
        if serializer.is_valid():
            name= serializer.validated_data.get('name')
            message = f'Hello {name}' # questo inserisce la variabile in una string
            return Response({'message':message})
        else:
            return Response(serializer.errors,
            status= status.HTTP_400_BAD_REQUEST
            ) #di defaul resoponse torna 200 che vuol dire ok, noi vogliamo torni un 400

    def put(self, request, pk=None): #pk is teh primary key, with put u update an object , in this case we dont update an object so pk=None
        """handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None ):
        """"handle a èartial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """delete object from database"""
        return Response({'method':'DELETE'})
