from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course, CourseSerializer
from django.http import Http404
from rest_framework import mixins, generics
from rest_framework.viewsets import ViewSet, ModelViewSet

# Create your views here.

#with modelViewSet
class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

#with viewset
'''
class CourseViewSet(ViewSet):
    def list(self, request):
        course = Course.objects.all()
        serialize= CourseSerializer(course, many = True)
        return Response(serialize.data)

    def create(self, request):
        serialize= CourseSerializer(data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialise.errors)

    def retrieve(self, request, pk):
        try:
            course =  Course.objects.get(pk = pk)
        except Course.DoesNotExist:
            raise Http404

        serialize = CourseSerializer(course)
        return Response(serialize.data)

    def destroy(self, request, pk):
        course = Course.objects.get(pk = pk)
        course.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
'''




#with combined generics
'''
class CourseView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
'''


#with generics
'''
class CourseView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetail(generics.RetrieveAPIView, generics.DestroyAPIView, generics.UpdateAPIView ):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
'''

#with Mixins
'''
class CourseView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class CourseDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)


    def put(self, request, pk):
        return self.update(request, pk)


    def delete(self, request, pk):
        return self.destroy(request, pk)
'''


#without Mixins
'''
class CourseView(APIView):

    def get(self, request):
        courses = Course.objects.all()
        serialize = CourseSerializer(courses, many = True)
        return Response(serialize.data)


    def post(self, request):
        serialise = CourseSerializer(data = request.data)
        if serialise.is_valid():
            serialise.save()
            return Response(serialise.data)
        else:
            return Response(serialise.errors)

class CourseDetail(APIView):

    def get_course(self, pk):
        try:
            return Course.objects.get(pk = pk)
        except Course.DoesNotExist:
            raise Http404

        return course

    def get(self, request, pk):
        course = self.get_course(pk)
        serialise = CourseSerializer(course)
        return Response(serialise.data)

    def put(self, request, pk):
        course = self.get_course(pk)
        serialise = CourseSerializer(course, data = request.data)
        if serialise.is_valid():
            serialise.save()
            return Response(serialise.data)
        else:
            return Response(serialise.errors)

    def delete(self, request, pk):
        course = self.get_course(pk)
        course.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
'''


