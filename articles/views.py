from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from articles.models import Article
from articles.serializers import ArticleSerializer
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

# @api_view(['GET', 'POST'])
# def articleAPI(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True) # many??
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     if request.method == 'POST':
#         serializer = ArticleSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class ArticleList(APIView):
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True) # many??
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ArticleSerializer)
    def post(self, request, format=None):
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def articleDetailAPI(request, article_id):
#     if request.method == 'GET':
#         article = get_object_or_404(Article, id=article_id)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         article = get_object_or_404(Article, id=article_id)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#     if request.method == 'DELETE':
#         article = get_object_or_404(Article, id=article_id)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class ArticleDetail(APIView):
    def get(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ArticleSerializer)
    def put(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
