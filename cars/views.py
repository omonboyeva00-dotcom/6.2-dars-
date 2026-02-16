from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


    def list(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)



    def retrieve(self, request, pk=None):
        try:
            car = Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return Response({"error": "Car not found"}, status=404)

        serializer = CarSerializer(car)
        return Response(serializer.data)



    def create(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def update(self, request, pk=None):
        try:
            car = Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return Response({"error": "Car not found"}, status=404)

        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)



    def partial_update(self, request, pk=None):
        try:
            car = Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return Response({"error": "Car not found"}, status=404)

        serializer = CarSerializer(car, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)



    def destroy(self, request, pk=None):
        try:
            car = Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return Response({"error": "Car not found"}, status=404)

        car.delete()
        return Response({"message": "Car deleted successfully"}, status=204)
