from rest_framework   import serializers


#keep all serializers in this file!!!

class HelloSerializer(serializers.Serializer):
    """serilizers  a namen field for testing APIView"""
    name = serializers.CharField(max_length=10)
    
