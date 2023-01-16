from rest_framework.response import Response
from rest_framework.decorators import api_view
from myblog.api.serializers import PostSerializer,PostDetailSerializer
from myblog.models import Post

@api_view(['GET'])
def get_post(request):
    post = Post.objects.all()
    serializer = PostSerializer(post, many = True)
    return Response({
        "data": serializer.data
    },200)

@api_view(['GET'])
def get_post_detail(request):
    id=request.GET.get('id')
    post = Post.objects.filter(id=id)
    if post:
        serializer = PostDetailSerializer(post, many = True)
        return Response({
            "data": serializer.data
        },200)
    else:
        return Response({
            "error": "please enter valid input"
        },422)


@api_view(['GET'])
def get_post_publish(request):
    post = Post.objects.filter(status=1)
    serializer = PostSerializer(post, many = True)
    return Response({
        "data": serializer.data
    },200)

@api_view(['DELETE'])
def delete_post(request):
    id=request.GET.get('id')
    post = Post.objects.filter(id=id).delete()
    if post:
        return Response({
            "message": "Deleted successfully"
        },200)
    else:
        return Response({
            "error": "Try again!"
        },422)

@api_view(['POST'])
def create_post(request):
    post = request.data
    serializers = PostDetailSerializer(data = post)
    if serializers.is_valid():
        serializers.save()
        return Response({
            "message": "Posted Successfully"
        },201)
    else:
        return Response({
            "error": serializers.errors #serializer itself throws error
        },422)
