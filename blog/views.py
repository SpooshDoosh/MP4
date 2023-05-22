from django.shortcuts import render, redirect
from .forms import SearchForm, CommentForm
from .models import BlogMod, CommentMod

# Create your views here.


def BlogListView(request):
    dataset = BlogMod.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            blog = BlogMod.objects.get(blog_title=title)
            return redirect(f'/blog/{blog.id}')
    else:
        form = SearchForm()
        template = 'blog/listview.html'
        context = {
            'dataset': dataset,
            'form': form,
        }
    return render(request, template, context)


def BlogDetailView(request, _id):
    try:
        data = BlogMod.objects.get(id=_id)
        comments = CommentMod.objects.filter(blog=data)
    except BlogModel.DoesNotExist:
        raise Http404('Data does not exist')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment = CommentMod(
                your_name=form.cleaned_data['your_name'],
                comment_body=form.cleaned_data['comment_body'], blog=data)
            Comment.save()
            return redirect(f'/blog/blogs/{_id}')
    else:
        form = CommentForm()

    template = 'blog/detailview.html'
    context = {
        'data': data,
        'form': form,
        'comments': comments,
    }
    return render(request, template, context)
