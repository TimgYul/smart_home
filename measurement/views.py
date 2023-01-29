# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer, SensorSerializer

        
class SensorGetView(ListCreateAPIView):
    queryset = Sensor.objects.all() 
    serializer_class = SensorDetailSerializer
    # добавление датчика
    def post(self, request):
        data = request.data
        Sensor(name=data.get('name'), description=data.get('description')).save()
        return Response('Датчик добавлен!')   
        
    
class CurrentSensor(RetrieveUpdateAPIView):
    queryset =  Sensor.objects.all() 
    serializer_class = SensorDetailSerializer
   
    # обновление описания датчика
    def patch(self, request,pk):
        sensor = self.get_object()
        data = request.data
        sensor.description = data.get('description')
        sensor.save()
        serializer = SensorDetailSerializer(sensor)
        return Response(serializer.data)
    
     # просмотр выбранного датчика
    def get(self, request, pk):
        sensor = self.get_object()
        ser = SensorDetailSerializer(sensor)
        return Response(ser.data)
    

class MeasurementGetView(CreateAPIView):
    queryset = Measurement.objects.all() 
    serializer_class = MeasurementSerializer
    
    # добавление измерения
    def post(self, request):
        data = request.data
        Measurement(sensors_id=data.get('sensor'),temperature=data.get('temperature')).save()
        # serializer = MeasurementSerializer(Measurement)
        return Response('OK!')


    