
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from onestart_rest.models import Snippet
from onestart_rest.serializer import SnippetSerializer


# Create your views here.


@api_view(['GET','POST'])
def snippet_list(request, format=None):
    """
        列出所有的代码片段,或者创建一个新的代码
       List all code snippets, or create a new snippet.
       """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


####  我们还需要一个与单个片段相对应的视图，并可用于检索，更新或删除代码段。####
@api_view(['GET', 'PUT', 'DELETE','UPDATE',])
def snippet_detail(request, pk, format=None):
    """
        检索,更新,或删除代码片段
      Retrieve, update or delete a code snippet.
      """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        seriaizer = SnippetSerializer(snippet)
        return Response(seriaizer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'UPDATE':
        pass