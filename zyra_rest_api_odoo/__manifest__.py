# -*- coding: utf-8 -*-
{
    'name': "REST API odoo",

    'summary': "Odoo REST API Manager with Auth APIs, API Keys, Rate Limits, and Full CRUD",

    'description': """
        REST API for Odoo.
        Build secure REST APIs with:
        - Auth APIs: login, register, reset password, user details
        - Model APIs with full CRUD (GET, POST, PUT/PATCH, DELETE)
        - Custom APIs with JSON or text responses
        - API key or session based authentication
        - Endpoint-level rate limiting and auth cooldown controls
        - Field selection, domain filtering, and related data support
    """,

    'author': "Zyra",
    'website': "",
    'support': "zyra88.ae@gmail.com",
    'category': 'Tools',
    'license': 'OPL-1',
    'currency': 'USD',
    'price': 50.0,
    'version': '1.0.0',
    'images': ['static/description/banner.png'],

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'data/auth_endpoint_data.xml',
        'views/app_key_views.xml',
        'views/auth_endpoint_views.xml',
        'views/model_endpoint_views.xml',
        'views/custom_endpoint_views.xml',
        'views/menu.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
