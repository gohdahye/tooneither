from django import forms

from toon.models import Toon


class ToonForm(forms.ModelForm):

    class Meta:
        model = Toon
        fields = ['title', 'content', 'head_image', 'file_image', 'day']
        labels = {
            'title' : '제목',
            'content' : '내용',
            'head_image' : '썸네일 이미지',
            'file_image' : '웹툰 파일',
            'day' : '요일'
        }