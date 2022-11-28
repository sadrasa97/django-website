from django.shortcuts import render,get_object_or_404
from blog.models import Post
# Create your views here.
def blog_view(request):
    posts=Post.objects.filter(status=1)# just published post
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    #post=Post.objects.all()# just published post
    post=get_object_or_404(Post,pk=pid)
    context={'post':post}
    return render(request,'blog/blog-single.html',context)

#def test(request):
#    posts=Post.objects.all()
#    context={'posts':posts}
#    return render(request,'test.html',context)
def test(request,name,family_name,age):
    #post=get_object_or_404(Post,pid)
    context={'name':name,'family_name':family_name,'age':age}
    return render (request,'test.html',context)