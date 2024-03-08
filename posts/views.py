from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from coupons.forms import CouponForm
from coupons.models import Coupon
from posts.forms import *
from posts.models import Post
from django.contrib import messages
from django.core.cache import cache

# Create your views here.

def index(request):
    user = request.user
    context = {
        'user':user,
    }
    return render(request,'posts/index.html',context)

def create(request):
    if request.method =='POST' and request.user.is_authenticated:
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            price = form.cleaned_data['price']
            post = Post.objects.create(user=request.user,
                                title=title,
                                content=content,
                                price=price)
            return redirect('posts:post',post.pk)
    else:
        form = PostForm()
    context = {
        'form':form,
    }
    return render(request,'posts/create.html',context)

def post(request, pk):
    post = cache.get('post_' + str(pk))
    if post is None:
        post = Post.objects.get(pk=pk)
        cache.set('post_' + str(pk), post)
    coupon_publish = Coupon_publish.objects.filter(post=post)
    cache.set('coupon_' + str(pk), coupon_publish)
    if request.method == 'POST' and request.user.is_authenticated:
        coupon_pk = request.POST.get('coupon_pk')
        coupon = Coupon_publish.objects.get(pk=coupon_pk)
        if not Coupon.objects.filter(user=request.user, publish_pk=coupon_pk).exists():
            if coupon.amount >= 1:
                post_instance = Post.objects.get(pk=post.pk)
                Coupon.objects.create(
                    post=post_instance,
                    user=request.user,
                    used_from=coupon.used_from,
                    used_to=coupon.used_to,
                    discount=coupon.discount,
                    used=True,
                    publish_pk=coupon_pk,
                )
                coupon.amount -= 1
                coupon.save()
                messages.success(request, '쿠폰이 발급되었습니다.')
            else:
                messages.warning(request, '쿠폰이 모두 떨어졌습니다.')
    context = {
        'post': post,
        'coupon': coupon_publish,
        'pk': pk,
    }
    return render(request, 'posts/post.html', context)





# def post(request,pk):
#     post = Post.objects.get(pk=pk)
#     coupon_publish = Coupon_publish.objects.filter(post=post)
#     if request.method == 'POST':
#         coupon_pk = request.POST.get('coupon_pk')
#         coupon = Coupon_publish.objects.get(pk=coupon_pk)
#         if not Coupon.objects.filter(user=request.user, publish_pk = coupon_pk).exists():
#             if coupon.amount >= 1:
#                 post_instance = Post.objects.get(pk=post.pk)
#                 Coupon.objects.create(
#                     post = post_instance,
#                     user = request.user,
#                     used_from = coupon.used_from,
#                     used_to = coupon.used_to,
#                     discount = coupon.discount,
#                     used = True,
#                     publish_pk = coupon_pk,
#                 )
#                 coupon.amount -= 1
#                 coupon.save()
#                 messages.success(request, '쿠폰이 발급되었습니다.')
#             else:
#                 messages.warning(request, '쿠폰이 모두 떨어졌습니다.')
#     context = {
#         'post':post,
#         'coupon':coupon_publish,
#         'pk':pk,
#     }
#     return render(request,'posts/post.html',context)