from django.urls import path
# from measurement.views import AddMeasurementView,SensorView, UpdateSensorView
from measurement.views import CurrentSensor, MeasurementGetView, SensorGetView
urlpatterns = [
    # path('demo/', demo)
    path('sensors/', SensorGetView.as_view()),
    path('sensors/<pk>/', CurrentSensor.as_view()),
    path('measurements/', MeasurementGetView.as_view())
    
    
    # path('sensors/', SensorView.as_view()),
    # path('sensors/<pk>/', UpdateSensorView.as_view()),
    # path('measurements/', AddMeasurementView.as_view())
]
