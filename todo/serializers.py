from asyncore import read
from rest_framework import serializers,status
from todo.models import Todo
class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(max_length=250)
    completed = serializers.BooleanField(default = False)

    def create(self, validated_data):
        todo,created = Todo.objects.get_or_create(**validated_data)
        if not created:
            raise ValueError(
                {"message":"Assignment already exists."},status.HTTP_409_CONFLICT
            )
        return todo