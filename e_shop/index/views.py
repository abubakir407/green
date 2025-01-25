from django.shortcuts import render, get_object_or_404, redirect
from .models import Picture
from .forms import CommentForm


# Create your views here.
def picture_list(request):
    pictures = Picture.objects.all()
    comment_form = CommentForm()
    return render(request, 'picture_list.html', {'pictures': pictures, 'comment_form': comment_form})

def like_picture(request, picture_id):
    picture = get_object_or_404(Picture, id=picture_id)
    picture.likes.create()
    return redirect('index:picture_list')

def add_comment(request, picture_id):
    picture = get_object_or_404(Picture, id=picture_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.picture = picture
            comment.save()
    return redirect('index:picture_list')
