from django.db import models
import uuid
import logging
from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger(__name__)


class Subject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True, verbose_name='Subject name')
    image = models.ImageField(verbose_name='Subject Image', upload_to='subject_images/')

    def __str__(self):
        return self.name


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True, verbose_name='Course name')
    subjects = models.ManyToManyField(Subject, related_name='courses')
    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True, verbose_name='Category Name')
    image = models.ImageField(verbose_name='Category Image', upload_to='category_images/')
    subject = models.ForeignKey(Subject, related_name='categories', on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, related_name="categories")
    parent_category = models.ForeignKey('self', null=True,
                                        blank=True, related_name='child_categories',
                                        on_delete=models.CASCADE)
    has_children = models.BooleanField(default=False)  # New field to track if category has children

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        try:
            previous_instance = self.__class__.objects.filter(pk=self.pk).first()
            previous_parent = previous_instance.parent_category if previous_instance else None

            if previous_parent:
                # If the category had a previous parent, update has_children of previous parent
                previous_parent.has_children = previous_parent.child_categories.exists()
                previous_parent.save()

            # Call the original save method to save the object
            super().save(*args, **kwargs)

            # If the category has a new parent, update the has_children field of the current parent
            if self.parent_category:
                self.parent_category.has_children = True
                self.parent_category.save()

        except self.__class__.DoesNotExist:
            # Handle DoesNotExist exception
            pass

        except Exception as e:
            # Handle other exceptions (including potential database connection errors)
            pass

class Theme(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True, verbose_name='Theme Name')
    text = models.TextField(verbose_name='Content text')
    category = models.ForeignKey(Category, related_name='themes',
                                 on_delete=models.CASCADE,)

    def __str__(self):
        return self.name


# class Content(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     theme = models.OneToOneField(Theme, related_name='content',
#                                  on_delete=models.CASCADE,
#                                  limit_choices_to={'content__isnull': True})
#     text = models.TextField(verbose_name='Content text')
#
#     def __str__(self):
#         return self.theme.name


class ThemeImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='content_images/')
    name = models.CharField(max_length=100)
    theme = models.ManyToManyField(Theme, related_name='images')

    def __str__(self):
        return self.name


class ThemeFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to='content_files/', verbose_name='Content file')
    name = models.CharField(max_length=255)
    theme = models.ManyToManyField(Theme, related_name='files')

    def __str__(self):
        return self.name


class ThemeVideoLink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    link = models.TextField(verbose_name='video link')
    name = models.CharField(max_length=100, blank=True, null=True)
    theme = models.ManyToManyField(Theme, related_name='video_links')

    def __str__(self):
        return self.name

