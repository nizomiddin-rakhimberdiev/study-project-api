from rest_framework import serializers
from .models import *


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'name']


class SubjectSerializerWithCourses(serializers.ModelSerializer):
    courses = CourseSerializer(many=True)

    class Meta:
        model = Subject
        fields = ['id', 'name', 'image', 'courses']


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ['id', 'name', 'image']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'has_children']


class CategorySerializerWithChildren(serializers.ModelSerializer):
    child_categories = CategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'subject', 'parent_category', 'has_children', 'child_categories']


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'


class CategoryWithThemesSerializer(serializers.ModelSerializer):
    themes = ThemeSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'themes']


class ContentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThemeImage
        fields = ['id', 'image', 'name']


class ContentFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThemeFile
        fields = ['id', 'file', 'name']


class ContentVideoLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThemeVideoLink
        fields = ['link', 'name']


class ThemeWithContentSerializer(serializers.ModelSerializer):
    images = ContentImageSerializer(many=True, read_only=True)
    files = ContentFileSerializer(many=True, read_only=True)
    video_links = ContentVideoLinkSerializer(many=True, read_only=True)

    class Meta:
        model = Theme
        fields = ['id', 'name', 'text', 'images', 'video_links', 'files']
