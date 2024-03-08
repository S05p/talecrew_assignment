from django import forms

from coupons.models import Coupon


class CouponForm(forms.Form):
    class Meta:
        model = Coupon