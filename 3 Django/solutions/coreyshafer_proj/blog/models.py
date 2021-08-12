from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    # title = #
    # content = #
    # date_posted = #
    # author = #foreignkey to user

    # write a def__str__ method to return the blog title


    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk': self.pk})
    pass