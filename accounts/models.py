from django.conf import settings
from django.db import models
from django.template.loader import render_to_string
from django.core.mail import send_mail
# Create your models here.


class UserStripe(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.stripe_id


class EmailConfirmed(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=200)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.confirmed)

    # send email and render string
    def active_user_email(self):
        activation_url = "http://localhost:8000/accounts/activate/%s" % (
            self.activation_key)
        context = {
            "activation_key": self.activation_key,
            "activation_url": activation_url,
            "user": self.user.username
        }
        message = render_to_string("accounts/activation_message.txt", context)
        subject = "Activate Your Email"
        print(message)
        # self.email_user(subject,message,settings.DEFAULT_FROM_EMAIL)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.user.email], **kwargs)
