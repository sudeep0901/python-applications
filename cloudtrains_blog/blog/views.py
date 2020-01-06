from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from future.types import newbytes
from taggit.models import Tag

from .models import Post
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm, SearchForm

from django.core.mail import send_mail
from django.db.models import Count


# Creating class based views

@login_required
class PostListView(ListView):
    queryset = Post.published.all()
    # can also use instead of above
    # model = Post
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


# Create your views here. function based views

@login_required
def post_list(request, tag_slug=None):
    posts = Post.published.all()

    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tag__in=[tag])

    print(posts)
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    print('*' * 50)
    print(posts)
    return render(request, 'blog/post/list.html',
                  {'page': page,
                   'posts': posts,
                   'tag': tag})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    # List of similar posts
    post_tags_ids = post.tag.values_list('id', flat=True)
    similar_posts = Post.published.filter(tag__in=post_tags_ids) \
        .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tag')) \
                        .order_by('-same_tags', '-publish')[:4]
    # List of Active Comments
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # Comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post/detail.html', {'post': post,
                                                     'comments': comments,
                                                     'new_comment': new_comment,
                                                     'comment_form': comment_form,
                                                     'similar_posts': similar_posts})


# sharing post via email

@login_required
def post_share(request, post_id):
    # retrive post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # Form submitted
        form = EmailPostForm(request.POST)
        print(dir(form))
        if form.is_valid():
            # form field passed validation
            cd = form.cleaned_data

            # ... send mail

            # send_mail('Django Mail', 'This is a test email', '@gmail.com',
            #           ['@gmail.com'], fail_silently=False)

            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading " {}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {} \n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com',
                      [cd['to']])
            sent = True

    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html',
                  {'post': post,
                   'form': form,
                   'sent': sent})


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # results = Post.objects.annotate(search=SearchVector('title', 'body'), ).filter(search=query)
            search_vector = SearchVector('title', 'body')
            search_query = SearchQuery(query)
            results = Post.objects.annotate(
                search=search_vector,
                rank=SearchRank(search_vector, search_query)
            ).filter(search=search_query).order_by('-rank')

            # Weighing vectors

            # search_vector = SearchVector('title', weight='A') + SearchVector('body',
            #                                                                  weight='B')
            # search_query = SearchQuery(query)
            # results = Post.objects.annotate(
            #     rank=SearchRank(search_vector, search_query)
            # ).filter(rank__gte=0.3).order_by('-rank')
    return render(request,
                  'blog/post/search.html',
                  {'form': form,
                   'query': query,
                   'results': results})
