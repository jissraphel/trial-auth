from django.conf.urls import url
from .views import (ExampleView,
		)

urlpatterns = [
    
    url(r'^$',ExampleView.as_view())
]