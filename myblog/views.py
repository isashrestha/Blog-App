from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status = 1).order_by('-created_at') 
    #Filter is applied, only the post with status published will be shown in the blog and latest post will be ontop(-)
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreate(generic.CreateView):
    model = Post
    fields = ["title", "author", "content",]
    