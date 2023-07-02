import io
from rest_framework.parsers import JSONParser
from snippets.serializers import SnippetSerializer

# Deserialize a single object
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
serializer = SnippetSerializer(data=data)
serializer.is_valid()
serializer.validated_data
serializer.save()

# Deserialize a queryset
serializer = SnippetSerializer(Snippet.objects.all(), many=True)
serializer.data
