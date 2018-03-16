from rest_framework import serializers
from recipies.models import Recipe
from accounts.models import UserAccount
from django.contrib.auth.models import User



class UserAccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    pk = serializers.IntegerField(source='user.pk', read_only=True)
    class Meta:
        model = UserAccount
        fields = ('username', 'pk', 'profilePic', 'aboutMe')



class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='user.username', read_only=True)
    profPic = serializers.ImageField(source='user.profInfo.profilePic', read_only=True)
    class Meta:
        model = Recipe
        fields = ('owner', 'profPic', 'name', 'instructions', 'ingredients',
        'created_at', 'about', 'cuisine', 'pic', 'like_id', 'save_id','cuisine', 'pk')
