from django.http import JsonResponse
from django.views import generic
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from cars.models import Car
from cars.forms import CarForm

import json


# Create your views here.
class CarView(generic.View):
    def get(self, request):
        name = request.GET.get("name", "World")
        return JsonResponse({"message": f"Hello, {name}!"})


class JSONResponseMixin:
    """
    A mixin that can be used to render a JSON response
    """

    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        return context


# This is not safe!!!!!!!!
@method_decorator(csrf_exempt, name="dispatch")
class CarCreateView(generic.View):
    form_class = CarForm

    def post(self, request, *args, **kwargs):
        # There's better ways to do this, but this is just for example
        body = request.body.decode("utf-8")
        data = json.loads(body)
        form = self.form_class(data)
        if form.is_valid():
            form.save()

            return JsonResponse({"message": "Car created successfully!"})
        return JsonResponse({"message": "Car created failed!"})


class CarListView(generic.View):
    def get(self, request):
        cars = Car.objects.all()
        return JsonResponse(
            {
                "message": "Cars retrieved successfully!",
                "cars": [
                    {
                        "name": car.name,
                        "color": car.color,
                        "price": car.price,
                    }
                    for car in cars
                ],
            }
        )
