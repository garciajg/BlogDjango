from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    """
    Gets a list of all the posts and 
    orders them from more recent to oldest
    """
    posts = Post.objects.filter(published_on__lte=timezone.now()).order_by('-published_on')
    return render(request, 'blog/post_list.html',{"posts":posts})