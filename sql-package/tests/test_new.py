from demo_app.models import Product
import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db

@pytest.mark.urls('demo_app.urls')
def test_demo(client, settings):
    settings.DEBUG = True
    url = reverse("test_endpoint")
    response = client.get(url)


    # qs = Product.objects.all().count()
    # assert qs == 0
    assert response.status_code == 200