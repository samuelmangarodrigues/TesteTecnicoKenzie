from urllib import response
from rest_framework.views import APIView,Request,Response,status
from todo.models import Todo
from todo.serializers import TodoSerializer

class TodoView(APIView):
    def get(self,_:Request):

        all_todo=Todo.objects.all()
        serialized = TodoSerializer(instance = all_todo, many=True)
    

        return Response(serialized.data,status.HTTP_200_OK)
    
    def post(self,request:Request):

        serialized = TodoSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)

        try:
            serialized.save()


            return Response(serialized.data,status.HTTP_201_CREATED)

        except ValueError as err:
            return Response(*err.args)