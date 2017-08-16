from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView,RetrieveUpdateDestroyAPIView

from home.api.serializers import (
	AnnotationsListSerializer,
	AnnotationsCreateSerializer,
	AnnotationsUpdateSerializer,
	AnnotationsRetrieveSerializer
)

from home.models import Annotations

class AnnotationsList(ListAPIView):
    queryset = Annotations.objects.all()
    serializer_class = AnnotationsListSerializer



class AnnotationsCreate(CreateAPIView):
    queryset = Annotations.objects.all()
    serializer_class = AnnotationsCreateSerializer




class AnnotationsUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Annotations.objects.all()
    serializer_class = AnnotationsUpdateSerializer




class AnnotationsRetrieve(RetrieveAPIView):
    queryset = Annotations.objects.all()
    serializer_class = AnnotationsRetrieveSerializer