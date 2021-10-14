from rest_framework import serializers

from api.models import Pars


class ParsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pars
        fields = '__all__'

    def create(self, validated_data):
        return Pars.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.usd_price = validated_data.get('usd_price', instance.usd_price)
        instance.city = validated_data.get('city', instance.city)
        instance.description = validated_data.get('description', instance.description)
        instance.id = validated_data.get('id', instance.id)
        instance.save()
        return instance




