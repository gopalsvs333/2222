from .views import StudentViewSet,SubjectViewSet
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Student',StudentViewSet)
router.register('Subject',SubjectViewSet)
# student_list=StudentViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# student_details=StudentViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#
#     'delete': 'destroy'
# })

urlpatterns = [
    # path('student/', student_list ,name='Student-list'),
    # path('student/<int:pk>/',student_details ,name='Student-details'),
      path('',include(router.urls)),

]