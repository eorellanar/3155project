from . import customers, menu_items, orders, order_details, recipes, sandwiches, resource_management

from ..dependencies.database import engine


def index():
    customers.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)
    orders.Base.metadata.create_all(engine)
    payment_information.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    ratings_reviews.Base.metadata.create_all(engine)
    resource_management.Base.metadata.create_all(engine)
