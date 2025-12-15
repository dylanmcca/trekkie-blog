from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = "trekkies/index.html"
    context_object_name = 'post_list'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('created_on')


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'trekkies/post_detail.html'
    slug_field = 'slug'
    context_object_name = 'post'