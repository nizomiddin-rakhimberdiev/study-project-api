from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.parsers import MultiPartParser, FormParser


class SubjectsCoursesView(APIView):
    def get(self, request):
        try:
            subjects = Subject.objects.prefetch_related('courses').all()
            subject_serializer = SubjectSerializerWithCourses(subjects, many=True)
            return Response(subject_serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class RelatedCategoriesAPIView(APIView):
    def get(self, request, subject_id, course_id):
        try:
            categories = Category.objects.filter(subject_id=subject_id, courses__id=course_id, parent_category__isnull=True)

            category_serializer = CategorySerializer(categories, many=True)
            subject_serializer = SubjectSerializer(Subject.objects.get(id=subject_id))
            course_serializer = CourseSerializer(Course.objects.get(id=course_id))

            response_data = {
                'subject': subject_serializer.data,
                'course': course_serializer.data,
                'categories': category_serializer.data
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CategoryWithChildrenView(APIView):
    def get(self, request, parent_category_id, course_id):
        try:
            parent_category = Category.objects.get(id=parent_category_id)
            course = Course.objects.get(id=course_id)

            parent_category_serializer = CategorySerializer(parent_category)
            subject_serializer = SubjectSerializer(parent_category.subject)
            course_serializer = CourseSerializer(course)

            child_categories = Category.objects.filter(parent_category=parent_category)
            child_category_serializer = CategorySerializer(child_categories, many=True)

            response_data = {
                'parent_category': parent_category_serializer.data,
                'subject': subject_serializer.data,
                'course': course_serializer.data,
                'categories': child_category_serializer.data
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({'error': 'Parent category does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Course.DoesNotExist:
            return Response({'error': 'Course does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class CategoryWithThemesView(APIView):
    def get(self, request, category_id):
        category = Category.objects.get(pk=category_id)
        serializer = CategoryWithThemesSerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ThemeWithContentView(APIView):
    def get(self, request, theme_id):
        theme = Theme.objects.get(pk=theme_id)
        serializer = ThemeWithContentSerializer(theme)
        return Response(serializer.data, status=status.HTTP_200_OK)




