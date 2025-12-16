from django.shortcuts import render, get_object_or_404
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

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )    