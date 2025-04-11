from django.shortcuts import render, redirect, get_object_or_404
from .models import Article  # 모델에서 Article이라는 클래스를 가져옴
from .forms import ArticleForm

# Create your views here.


def index(request):
    articles = (
        Article.objects.all()
    )  # articles 는 클래스 Articles의 모든 정보를 가져옴?
    context = {
        "articles": articles,  # 딕셔너리 형태로 감싸서 사용, "a" 가되어도 상관없음
    }
    return render(
        request, "articles/index.html", context
    )  # context 안에 있는 정보를 index.html로 넘김


def create(request):
    if (
        request.method == "POST"
    ):  # 요청 받는 형식이 수정 생성 타입이면~ 아래 내용을 실행해라?
        form = ArticleForm(request.POST)  # <- 잘모름
        if form.is_valid():  # form이 유효한가?
            article = form.save()  # 모름
            return redirect("articles:index")
    else:
        form = ArticleForm()
    return render(request, "articles/form.html", {"form": form})  
    # from.html에 form 이라는 이름으로 객체를 넘겨줌


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "articles/detail.html", {"article": article})


def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("articles:detail", article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, "articles/form.html", {"form": form})


def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('articles:index')
