from django.http import HttpResponse
from .models import MyModel
import datetime

def create_model_instance(request):
    print(f"View started at {datetime.datetime.now()}")
    obj = MyModel.objects.create(name="Test Instance")
    # obj.save()
    print(f"View finished at {datetime.datetime.now()}")
    return HttpResponse("Check the console for timestamp logs")








