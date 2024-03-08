from django.test import TestCase
from django.urls import reverse
from accounts.models import User
from coupons.models import Coupon
from .models import *

class PostViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345',birthday='2000-01-01')
        self.client.login(username='testuser', password='12345')
        self.post = Post.objects.create(user=self.user, title='Test Post', content='This is a test post.', price=10)

    def test_post_view(self):
        response = self.client.get(reverse('posts:post', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post.html')

    def test_coupon_publishing(self):
        coupon_publish = Coupon_publish.objects.create(post=self.post, amount=5, used_from='2024-03-08',
                                                       used_to='2024-03-15', discount=5)
        response = self.client.post(reverse('posts:post', kwargs={'pk': self.post.pk}),
                                    {'coupon_pk': coupon_publish.pk})
        self.assertEqual(response.status_code, 302)  # Redirects back to the post page after coupon issuance

        # Check if the coupon is properly created
        coupon = Coupon.objects.filter(post=self.post, user=self.user).first()
        self.assertIsNotNone(coupon)
        self.assertEqual(coupon.post, self.post)
        self.assertEqual(coupon.user, self.user)
        self.assertEqual(coupon.used_from, coupon_publish.used_from)
        self.assertEqual(coupon.used_to, coupon_publish.used_to)
        self.assertEqual(coupon.discount, coupon_publish.discount)
        self.assertTrue(coupon.used)

        # Check if the coupon amount is decreased
        updated_coupon_publish = Coupon_publish.objects.get(pk=coupon_publish.pk)
        self.assertEqual(updated_coupon_publish.amount, 4)  # One coupon is used, so the amount should decrease by 1


