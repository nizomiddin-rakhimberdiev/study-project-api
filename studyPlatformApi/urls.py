from django.urls import path
from .views import *

urlpatterns = [
    path('subjects-courses/', SubjectsCoursesView.as_view(), name='subject-list'),
    path('related-categories/<uuid:subject_id>/<uuid:course_id>/', RelatedCategoriesAPIView.as_view(), name='related_categories'),
    path('categories-with-parent-category/<uuid:parent_category_id>/<uuid:course_id>/', CategoryWithChildrenView.as_view(), name='category-with-children'),
    path('category/<uuid:category_id>/themes/', CategoryWithThemesView.as_view(), name='theme-list'),
    path('theme/<uuid:theme_id>/', ThemeWithContentView.as_view(), name='content'),
]
