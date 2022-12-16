# def test_example():
#     assert 1==2
from ecommerce.inventory.models import Product


def test_insert_single_product_with_sub_category(single_product):
    new_product=single_product 
    get_product=Product.objects.all().first() 
    assert new_product.id == get_product.id 
    print(get_product.category.name)
    
# def test_create_category_with_child(category_with_child):
#     new_sub_category= category_with_child 
#     get_category=Category.objects.all().first() 
#     assert get_category.children.first().id == new_sub_category.id 
    
    
    