from rest_framework import viewsets
from nglib.views import get_author_books, get_author_id
from nglib.forms import isStandardized
from rest_framework.response import Response
from rest_framework.views import APIView
from nglib.models import SearchStats
class DataDispatcher(APIView):

    def get(self, request):
        
        name = self.request.query_params.get('name', None)
        surname = self.request.query_params.get('surname', None)
        author_id = self.request.query_params.get('author_id', None)
        stats = self.request.query_params.get('stats', None)
        
        if name is not None and surname is not None:
            if isStandardized(name) and isStandardized(surname):
                return Response(get_author_id(name, surname))
            else: 
                return Response({'error':'wrong data'})
        if author_id is not None:
            return Response(get_author_books(author_id))
        else:
            return Response({'api/?name=J%20K&surname=Rowling - get author info':'api/?author_id=OL23919A - get books'})
       
