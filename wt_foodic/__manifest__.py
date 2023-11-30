# -*- coding: utf-8 -*-
# Part of Odoo. See COPYRIGHT & LICENSE files for full copyright and licensing details.

{
    "name": "Foodics Odoo Connector",
    "version": "1.0",
    "category": "Point Of Sale",
    "summary": "Sync data from foodics to odoo",
    "description": """
        With this application user will be able to sync branches, payment methods, categories, products and orders from foodics to odoo.
        from date and to date functionality.
    """,
    "author": "Warlock Technologies Pvt Ltd.",
    "website": "http://warlocktechnologies.com",
    "support": "info@warlocktechnologies.com",
    "depends": ["product", "point_of_sale", "account"],
    "data": [
        'security/ir.model.access.csv',
        'data/cron.xml',
        'wizard/message_view.xml',
        'views/connector_view.xml',
        'views/branches_view.xml',
        'views/payment_methods_view.xml',
        'views/categories_view.xml',
        'views/pos_orders_view.xml',
        'views/purchase_order_views.xml',
        'wizard/foodic_operation_views.xml'
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
    "price": 300,
    "currency": "USD",
    "images": ['static/image/screen_image.png'],
    "license": "OPL-1",
}

