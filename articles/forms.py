from django import forms
from .models import Article  # 아래에서 Article을 사용하기 때문에 models에서 가져옴


class ArticleForm(
    forms.ModelForm
):  # 괄호안의 내용은 필요에 따라 변경될 수 있으나 어떤역할인지 모르곘음
    class Meta:
        model = Article  # Article을 참조?
        fields = [
            "title",
            "content",
        ]  # 필드값 안의 내용은 내가 Articles 클래스 안에서 선택 가능
