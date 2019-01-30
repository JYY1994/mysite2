from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import BlogArticles

def blog_title(request):
    """响应文章标题"""
    blogs = BlogArticles.objects.all()
    return render(request,"blog/titles.html",{"blogs":blogs})

def blog_article(request,article_id):
    """响应文章内容"""
    #article = BlogArticles.objects.get(id = article_id)
    article = get_object_or_404(BlogArticles,id = article_id)
    pub = article.publish
    return render(request, "blog/content.html",{"article":article,"publish":pub})