from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from ecommerce.inventory.models import ProductInventory

@registry.register_document
class Product
