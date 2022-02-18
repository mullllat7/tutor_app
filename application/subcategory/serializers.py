from rest_framework import serializers

from application.subcategory.models import Subcategory, SubcategoryImage


class SubcatSerializers(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = SubcatImageSerializer(SubcategoryImage.objects.filter(subcategory=instance.id, ), many=True, context=self.context).data
        return representation
class SubcatImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubcategoryImage
        fields = ('image', )

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation


class SubcatDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        total_rating = [i.rating for i in instance.comment.all()]
        if len(total_rating) > 0:
            representation['total_rating'] = sum(total_rating) / len(total_rating)
        representation['images'] = SubcatImageSerializer(SubcategoryImage.objects.filter(clothes=instance.id,), many=True, context=self.context).data
        return representation
