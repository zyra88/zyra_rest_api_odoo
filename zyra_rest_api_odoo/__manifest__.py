# -*- coding: utf-8 -*-
{
    'name': "Odoo REST API",

    'summary': "API, REST API, Odoo REST API, REST API for Odoo with Auth, API Keys, and Full CRUD",

    'description': """
        Odoo REST API.
        REST API for Odoo with full API management.
        Build secure REST APIs with:
        - Auth APIs: login, register, reset password, user details
        - Model APIs with full CRUD (GET, POST, PUT/PATCH, DELETE)
        - Custom APIs with JSON or text responses
        - API key or session based authentication
        - Endpoint-level rate limiting and auth cooldown controls
        - Field selection, domain filtering, and related data support
        Keywords: API, REST API, Odoo REST API, REST API for Odoo
    """,

    'author': "Zyra",
    'website': "https://www.zyra.com",
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
