from django.shortcuts import render
from .models import Article, Reporter

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year = year)
    context = {
        'year': year, 
        'article list': a_list
    }
    return render(request, 'news/year_archive.html', context)

def month_archive(request, year, month):
    a_list = Article.objects.filter(pub_date__month = month)
    context = {
        'year': year,
        'month': month, 
        'article list': a_list
    }
    return render(request, 'news/month_archive.html', context)

def article_detail(request, year, month, pk):
    # a_list = Article.objects.filter(pub_date = year)
    context = {
        'year': year,
        'month': month,
        'pk': pk,
        # 'article list': a_list
    }
    return render(request, 'news/article_detail.html', context)

def user_list(request):
    list = Reporter.objects.all().order_by('-id').reverse()
    data = {'list': list}
    return render(request, 'news/user_list.html', data)
