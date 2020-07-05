import serpy


class UserProfileSerializer(serpy.Serializer):
    id = serpy.Field()
    username = serpy.Field()
    email = serpy.Field()
    first_name = serpy.Field()
    last_name = serpy.Field()


class UserAutentication(serpy.Serializer):
    id = serpy.MethodField()
    username = serpy.MethodField()
    email = serpy.MethodField()
    first_name = serpy.MethodField()
    last_name = serpy.MethodField()
    token = serpy.MethodField()

    def get_id(self, obj):
        if obj.user is not None:
            return obj.user_id

    def get_username(self, obj):
        if obj.user is not None:
            return obj.user.username

    def get_email(self, obj):
        if obj.user is not None:
            return obj.user.email

    def get_first_name(self, obj):
        if obj.user is not None:
            return obj.user.first_name

    def get_last_name(self, obj):
        if obj.user is not None:
            return obj.user.last_name

    def get_token(self, obj):
        if obj is not None:
            return obj.key
