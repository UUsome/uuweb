import json
from django.http import JsonResponse
from blog.models import Article, Comment
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
import markdown


# 框架列表 全部

def blog_list(request):
    context = {}
    _blog_list = Article.objects.all().order_by('-date_time')
    _blog_hot = Article.objects.all().order_by('-view')
    context = {}
    context['blog_list'] = _blog_list
    context['blog_hot'] = _blog_hot
    return render(request, 'blog/index.html', context)


def category(request, name):
    """
    分类
    :param request:
    :param name:
    :return:
    """
    _blog_list = Article.objects.filter(category__name=name)
    context = {}
    context['blog_list'] = _blog_list
    context['category'] = name
    return render(request, 'blog/category.html', context)


def tag(request, name):
    """
    标签
    :param request:
    :param name
    :return:
    """
    _blog_list = Article.objects.filter(tag__tag_name=name)
    context = {}
    context['blog_list'] = _blog_list
    context['tag'] = name
    return render(request, 'blog/tag.html', context)


def archive(request):
    """
    文章归档
    :param request:
    :return:
    """
    _blog_list = Article.objects.values("id", "title", "date_time").order_by('-date_time')
    archive_dict = {}
    for blog in _blog_list:
        pub_month = blog.get("date_time").strftime("%Y年%m月")
        if pub_month in archive_dict:
            archive_dict[pub_month].append(blog)
        else:
            archive_dict[pub_month] = [blog]
    data = sorted([{"date": _[0], "blogs": _[1]} for _ in archive_dict.items()], key=lambda item: item["date"],
                  reverse=True)
    return render(request, 'blog/archive.html', {"data": data})


def detail(request, pk):
    """
    博文详情
    :param request:
    :param pk:
    :return:
    """
    article = Article.objects.get( pk=pk)
    # 将markdown语法渲染成html样式
    article.content = markdown.markdown(article.content,
        extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        ])
    article.viewed()
    context = {}
    context['blog'] = article
    return render(request, 'blog/detail.html',context)
    
    
def articleadd(request):
    case_contents_count = request.POST.get("case_contents_count")
    unique_string = str(uuid.uuid4())
    SolutionI = Solution()
    SolutionI.uniqueid = unique_string
    SolutionI.case_id = Case_title_id
    SolutionI.is_title = 1
    SolutionI.solution = request.POST.get("solution0")
    SolutionI.save()

    return redirect(to='caselist')
