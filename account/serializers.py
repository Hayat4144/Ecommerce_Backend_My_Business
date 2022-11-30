

from dataclasses import fields
from rest_framework import serializers
from account.models import User


# registration serializer
class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password',
                  'confirm_password', 'mobile_no', 'full_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            full_name=self.validated_data['full_name'],
            mobile_no=self.validated_data['mobile_no'],

        )

        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError(
                {"password": "Passwords doesn't match."})

        user.set_password(password)
        user.save()
        return user


# forget password serializer
class ChangePasswordSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    new_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['confirm_password', 'new_password', 'password']

    def validatepassword(self):
        new_password = self.validated_data['new_password']
        confirm_password = self.validated_data['confirm_password']
        password = self.validated_data['password']

        if new_password == password:
            raise serializers.ValidationError(
                {"error": "Your New Password  match with old password."})

        if new_password != confirm_password:
            raise serializers.ValidationError(
                {"password": "Password doesn't match."})

        if len(new_password) < 6 or len(new_password) > 16:
            raise serializers.ValidationError(
                {"error": "password should be between 8 and 16 characters long"})

        if not any(x.isupper() for x in new_password):
            raise serializers.ValidationError(
                {"error": "password should have at least one upper case alphabet"})

        if not any(x.islower() for x in new_password):
            raise serializers.ValidationError(
                {"error": "password should have at least one lower case alphabet"})

        if not any(x.isdigit() for x in new_password):
            raise serializers.ValidationError(
                {"error": "password should have at least one number"})

        valid_special_characters = {'@', '_', '!', '#', '$', '%', '^', '&', '*', '(', ')',
                                    '?', '/', '|', '{', '}', '~', ':'}

        if not any(x in valid_special_characters for x in new_password):
            raise serializers.ValidationError(
                {"error": "password should have at least one special character"})


class ResetPasswordSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    new_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['confirm_password', 'new_password']

    def validatepassword(self):
        new_password = self.validated_data['new_password']
        confirm_password = self.validated_data['confirm_password']

        if new_password != confirm_password:
            raise serializers.ValidationError(
                {"password": "Password doesn't match."})

        if len(new_password) < 6 or len(new_password) > 16:
            raise serializers.ValidationError(
                {"error": "password should be between 8 and 16 characters long"})

        if not any(x.isupper() for x in new_password):
            raise serializers.ValidationError(
                {"error": "password should have at least one upper case alphabet"})

        if not any(x.islower() for x in new_password):
            raise serializers.ValidationError(
                {"error": "password should have at least one lower case alphabet"})

        if not any(x.isdigit() for x in new_password):
            raise serializers.ValidationError(
                {"error": "password should have at least one number"})

        valid_special_characters = {'@', '_', '!', '#', '$', '%', '^', '&', '*', '(', ')',
                                    '?', '/', '|', '{', '}', '~', ':'}

        if not any(x in valid_special_characters for x in new_password):
            raise serializers.ValidationError(
                {"error": "password should have at least one special character"})
