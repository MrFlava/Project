from rest_framework import serializers

from main.models import Portfolio, Image, Comment


class PortfolioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portfolio
        exclude = ['profile']


class ImageSerializer(serializers.ModelSerializer):
    portfolio_name = serializers.CharField(source='portfolio.name', read_only=True)

    class Meta:
        model = Image
        fields = ['id', 'name', 'description', 'image', 'created_date', 'portfolio', 'portfolio_name']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        exclude = ['profile', 'image']


