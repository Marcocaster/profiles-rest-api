from rest_framework.views  import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test APIView"""
    def get(self, request,format=None):
        """return a list of APIView features"""
        an_apiview = [
            "USes HTTP methods as function (get, post, put, delete)",
            "IS similar to a traditional DJango view",
            "Gives you teh most control over your application logic",
            "is mapped manually to URLs" ,
        ]
        return Response({"message":"hello", "an_apiview":an_apiview}) 
