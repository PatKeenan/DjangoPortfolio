from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Language(models.Model):
    language = models.CharField(verbose_name="Language", max_length=50)
    
    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"
        ordering = ['-language']

    def __str__(self):
        return self.language


class Category(models.Model):
    category = models.CharField(verbose_name="Language", max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['-category']

    def __str__(self):
        return self.category

class BlogPost(models.Model):
    title = models.CharField(verbose_name="Title",
                             max_length=60, unique=True,)
    slug = models.SlugField(max_length=500, unique=True, blank=True)
    description = models.CharField(
        verbose_name="Brief Description", max_length=150, default="")
    featured_image = models.ImageField("Featured Image", upload_to="images/")
    image_description = models.CharField(
        verbose_name="Image Description", max_length=400, default="")
    langs = models.ManyToManyField(Language, verbose_name="languages", blank=True)
    cats = models.ManyToManyField(
        Category, verbose_name="category", blank=True)
    github_link = models.CharField(
        verbose_name="Github Link", max_length=400, blank=True, null=True)
    project_link = models.CharField(
        verbose_name="ProjectLink", max_length=200, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(verbose_name ="Featured Post", default=False, blank=True)
    body = RichTextUploadingField(blank=True, null=True)
    
    
    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["-date_added"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  # new
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"slug": self.slug})

class Project(models.Model):
    title = models.CharField(verbose_name="Title", max_length=60)
    slug = models.SlugField(max_length=500, unique=True, blank=True)
    description = models.CharField(
        verbose_name="Brief Description", max_length=150, default="")
    featured_image = models.ImageField("Featured Image", upload_to="images")
    image_description = models.CharField(
        verbose_name="Image Description", max_length=400, default="")
    langs = models.ManyToManyField(
        Language, verbose_name="languages", blank=True)
    cats = models.ManyToManyField(
        Category, verbose_name="category", blank=True)
    github_link = models.CharField(
        verbose_name="Github Link", max_length=200, blank=True, null=True)
    project_link = models.CharField(
        verbose_name="ProjectLink", max_length=200, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(verbose_name="Featured Post",
                        default=False, blank=True)
    body = RichTextUploadingField(blank=True, null=True)
    

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["-date_added"]

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):  # new
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("project-detail", kwargs={"slug": self.slug})
