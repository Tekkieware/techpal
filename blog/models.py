from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.utils import timezone
from django.core.mail import EmailMessage
from django.template.loader import render_to_string, get_template
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.

class User(AbstractUser):
    pass

class Post(models.Model, HitCountMixin):
    POST_TYPE_CHOICE = (
        ('Howto', 'How to accomplish tasks'),
        ('News', 'Tech News'),
        ('Articles','Tech and Programming articles')
    )
    post_type = models.CharField(max_length=50, null=False, blank=False, choices= POST_TYPE_CHOICE)
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    content = RichTextUploadingField(null= False, blank= False, config_name='default')
    created  = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now = True)
    slug = models.SlugField(unique = False)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Post, self).save()

    class Meta:
        ordering = ['-created']

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add= True)
    text = models.TextField(max_length = 200, blank = False, null = False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.text

class Question(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add= True)
    text = models.TextField(max_length = 200, blank = False, null = False)
    slug = models.SlugField(unique = False)
    replied = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.text)
        return super(Question, self).save()


class Reply(models.Model):
    question = models.OneToOneField(Question, on_delete= models.CASCADE)
    content = RichTextField(null= False, blank = False, config_name= 'special')

    def save(self, *args, **kwargs):      
        self.question.replied = True 
        self.question.save()
        ctx = {'question':self.question.text, 'content':self.content}
        html_message = get_template('blog/email.html').render(ctx)
        subject ='Hello ' + self.question.user.username + ': Reply To your Question at TechPAL'
        msg = EmailMessage(subject, html_message, 'Tekkieware@gmail.com', [self.question.user.email])
        msg.content_subtype = "html" # Main content is now text/html
        msg.send()
        return super(Reply, self).save()