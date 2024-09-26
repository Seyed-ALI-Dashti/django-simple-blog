from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

# posts = {
#     "post1": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquam commodi cumque cupiditate enim eos est et facere fuga itaque iusto labore laborum minima molestias, nam neque nihil nisi non obcaecati officia placeat porro possimus, praesentium quam quibusdam quis quod repudiandae saepe sed sint sit soluta ullam ut voluptates voluptatibus.",
#     "post2": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquam commodi cumque cupiditate enim eos est et facere fuga itaque iusto labore laborum minima molestias, nam neque nihil nisi non obcaecati officia placeat porro possimus, praesentium quam quibusdam quis quod repudiandae saepe sed sint sit soluta ullam ut voluptates voluptatibus.",
#     "post3": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquam commodi cumque cupiditate enim eos est et facere fuga itaque iusto labore laborum minima molestias, nam neque nihil nisi non obcaecati officia placeat porro possimus, praesentium quam quibusdam quis quod repudiandae saepe sed sint sit soluta ullam ut voluptates voluptatibus.",
#     "post4": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquam commodi cumque cupiditate enim eos est et facere fuga itaque iusto labore laborum minima molestias, nam neque nihil nisi non obcaecati officia placeat porro possimus, praesentium quam quibusdam quis quod repudiandae saepe sed sint sit soluta ullam ut voluptates voluptatibus.",
#     "post5": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquam commodi cumque cupiditate enim eos est et facere fuga itaque iusto labore laborum minima molestias, nam neque nihil nisi non obcaecati officia placeat porro possimus, praesentium quam quibusdam quis quod repudiandae saepe sed sint sit soluta ullam ut voluptates voluptatibus.",
#     "post6": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquam commodi cumque cupiditate enim eos est et facere fuga itaque iusto labore laborum minima molestias, nam neque nihil nisi non obcaecati officia placeat porro possimus, praesentium quam quibusdam quis quod repudiandae saepe sed sint sit soluta ullam ut voluptates voluptatibus.",
#     "post7": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquam commodi cumque cupiditate enim eos est et facere fuga itaque iusto labore laborum minima molestias, nam neque nihil nisi non obcaecati officia placeat porro possimus, praesentium quam quibusdam quis quod repudiandae saepe sed sint sit soluta ullam ut voluptates voluptatibus.",
# }
posts = {
    "post1": {
        "body": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquam commodi cumque cupiditate enim eos est et facere fuga itaque iusto labore laborum minima molestias, nam neque nihil nisi non obcaecati officia placeat porro possimus, praesentium quam quibusdam quis quod repudiandae saepe sed sint sit soluta ullam ut voluptates voluptatibus.",
        "author": "Ali Dashti",
        "date": "September 26 2024",
    },
    "post2": {
        "body": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquam commodi cumque cupiditate enim eos est et facere fuga itaque iusto labore laborum minima molestias, nam neque nihil nisi non obcaecati officia placeat porro possimus, praesentium quam quibusdam quis quod repudiandae saepe sed sint sit soluta ullam ut voluptates voluptatibus.",
        "author": "Ali Dashti",
        "date": "September 26 2024",
    },
    "post3": {
        "body": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquam commodi cumque cupiditate enim eos est et facere fuga itaque iusto labore laborum minima molestias, nam neque nihil nisi non obcaecati officia placeat porro possimus, praesentium quam quibusdam quis quod repudiandae saepe sed sint sit soluta ullam ut voluptates voluptatibus.",
        "author": "Ali Dashti",
        "date": "September 26 2024",
    },
    "post4": {
        "body": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquam commodi cumque cupiditate enim eos est et facere fuga itaque iusto labore laborum minima molestias, nam neque nihil nisi non obcaecati officia placeat porro possimus, praesentium quam quibusdam quis quod repudiandae saepe sed sint sit soluta ullam ut voluptates voluptatibus.",
        "author": "Ali Dashti",
        "date": "September 26 2024",
    },
    "post5": {
        "body": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquam commodi cumque cupiditate enim eos est et facere fuga itaque iusto labore laborum minima molestias, nam neque nihil nisi non obcaecati officia placeat porro possimus, praesentium quam quibusdam quis quod repudiandae saepe sed sint sit soluta ullam ut voluptates voluptatibus.",
        "author": "Ali Dashti",
        "date": "September 26 2024",
    },
    "post6": {
        "body": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquam commodi cumque cupiditate enim eos est et facere fuga itaque iusto labore laborum minima molestias, nam neque nihil nisi non obcaecati officia placeat porro possimus, praesentium quam quibusdam quis quod repudiandae saepe sed sint sit soluta ullam ut voluptates voluptatibus.",
        "author": "Ali Dashti",
        "date": "September 26 2024",
    },
    "post7": {
        "body": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquam commodi cumque cupiditate enim eos est et facere fuga itaque iusto labore laborum minima molestias, nam neque nihil nisi non obcaecati officia placeat porro possimus, praesentium quam quibusdam quis quod repudiandae saepe sed sint sit soluta ullam ut voluptates voluptatibus.",
        "author": "Ali Dashti",
        "date": "September 26 2024",
    },
    "post8": {
        "body": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquam commodi cumque cupiditate enim eos est et facere fuga itaque iusto labore laborum minima molestias, nam neque nihil nisi non obcaecati officia placeat porro possimus, praesentium quam quibusdam quis quod repudiandae saepe sed sint sit soluta ullam ut voluptates voluptatibus.",
        "author": "Ali Dashti",
        "date": "September 26 2024",
    },

}

# Create your views here.

def index(request):
    posts_fetch = list(posts.keys())
    return render(request, 'blog/index.html', {'posts': posts_fetch})


def post(request, post):

    if (post in posts):
        post_fetch = posts[post]
        body_fetch = post_fetch['body']
        author_fetch = post_fetch['author']
        date_fetch = post_fetch['date']
        return render(request, 'blog/post.html', {
            'post': post, 'post_fetch': post_fetch,
            'body': body_fetch,
            'author': author_fetch,
            'date': date_fetch
        })
    else:
        raise Http404()
