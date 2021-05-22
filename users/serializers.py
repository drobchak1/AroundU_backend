from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from versatileimagefield.serializers import VersatileImageFieldSerializer 

class UserSerializer(serializers.ModelSerializer):
    events = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    visitors = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
        ],
        allow_null=True,
        required=False
    )
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "image",
            "bio",
            "city",
            "phone",
            "events",
            "visitors",
        ]
        extra_kwargs = {
            "first_name": {"required": False},
            "last_name": {"required": False},
            "image": {"required": False},
            "bio": {"required": False},
            "city": {"required": False},
            "phone": {"required": False},
            "events": {"required": False},
            "visitors": {"required": False},
        }
        
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
        ],
        allow_null=True,
        required= False
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(write_only=True, allow_null=True, allow_blank=True, required= False)
    last_name = serializers.CharField(write_only=True, allow_null=True, allow_blank=True, required= False)
    bio = serializers.CharField(write_only=True, allow_null=True, allow_blank=True, required= False)
    city = serializers.CharField(write_only=True, allow_null=True, allow_blank=True, required= False)
    phone = serializers.CharField(write_only=True, allow_null=True, allow_blank=True, required= False)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'image', 'bio', 'city', 'phone')
        extra_kwargs = {
            "first_name": {"required": False},
            "last_name": {"required": False},
            "image": {"required": False},
            "bio": {"required": False},
            "city": {"required": False},
            "phone": {"required": False},
            "events": {"required": False},
            "visitors": {"required": False},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', None),
            last_name=validated_data.get('last_name', None),
            image=validated_data.get('image', None),
            bio=validated_data.get('bio', None),
            city=validated_data.get('city', None),
            phone=validated_data.get('phone', None),
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance

class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
        ],
        allow_null=True
    )
    first_name = serializers.CharField(write_only=True, allow_null=True)
    last_name = serializers.CharField(write_only=True, allow_null=True)
    bio = serializers.CharField(write_only=True, allow_null=True)
    city = serializers.CharField(write_only=True, allow_null=True)
    phone = serializers.CharField(write_only=True, allow_null=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'image', 'bio', 'city', 'phone')
        # extra_kwargs = {
        #     'first_name': {'required': True},
        #     'last_name': {'required': True},
        # }

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.username = validated_data['username']
        instance.image = validated_data['image']
        instance.bio = validated_data['bio']
        instance.city = validated_data['city']
        instance.phone = validated_data['phone']

        instance.save()

        return instance