from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, HyperlinkedRelatedField, \
    SerializerMethodField
from home.models import Annotations


class AnnotationsListSerializer(ModelSerializer):
    class Meta:
        model = Annotations
        fields = ("src","text","shape_type","x","y","width","height")

class AnnotationsCreateSerializer(ModelSerializer):
    class Meta:
        model = Annotations
        fields = ("src","text","shape_type","x","y","width","height")

class AnnotationsUpdateSerializer(ModelSerializer):
    class Meta:
        model = Annotations
        fields = ("src","text","shape_type","x","y","width","height")

class AnnotationsRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Annotations
        fields = ("src","text","shape_type","x","y","width","height")