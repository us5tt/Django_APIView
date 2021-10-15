from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import render


from .models import Pars
from .serializers import ParsSerializer


def index(request):
    return render(request, "api/index.html")


class ParsView(APIView):
    def get(self, request):
        items = Pars.objects.all()
        serializer = ParsSerializer(items, many=True)
        return Response({"items": serializer.data})

    def post(self, request):
        items = request.data.get('items')
        serializer = ParsSerializer(data=items)
        if serializer.is_valid(raise_exception=True):
            items_saved = serializer.save()
        return Response({"success": "Items '{}' created successfully".format(items_saved.title)})

    def put(self, request, pk):
        saved_items = get_object_or_404(Pars.objects.all(), pk=pk)
        data = request.data.get('items')
        serializer = ParsSerializer(instance=saved_items, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            items_saved = serializer.save()
        return Response({
            "success": "Items '{}' updated successfully".format(items_saved.title)
        })

    def delete(self, request, pk):
        article = get_object_or_404(Pars.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Items with id `{}` has been deleted.".format(pk)
        }, status=204)


