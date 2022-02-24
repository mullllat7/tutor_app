from rest_framework import serializers

from application.theme.models import Theme, ThemeImage


class ThemeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Theme
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation

class ThemeDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Theme
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation


class SubcatImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ThemeImage
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

