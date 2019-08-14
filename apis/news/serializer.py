from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from apis.news.models import News
from django.utils.text import slugify

class NewsSerializer(serializers.ModelSerializer):
    slug    =   serializers.CharField(required=False)

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        context     =   kwargs.get('context')
        if context:
            self.request    =   context.get('request')

    class Meta:
        model       =   News 
        fields      =   ['pk','title','story','slug','category','author']
    
    def create(self, validated_data):
        title       =   validated_data.get('title')
        slug        =   slugify(title)
        news        =   News(**validated_data)
        news.slug   =   slug
        news.author =   self.request.user
        news.save()
        return news

    # def update(self, instance, validated_data):
    #     instance.title          =   validated_data.get("title", instance.title)
    #     instance.story          =   validated_data.get("story", instance.story)
    #     instance.category          =   validated_data.get("category", instance.category)
    #     # instance.cover_image          =   validated_data.get("cover_image",instance.cover_image)
    #     return instance


