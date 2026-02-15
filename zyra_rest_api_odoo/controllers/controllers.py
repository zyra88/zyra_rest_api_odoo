# -*- coding: utf-8 -*-
from odoo import http


class ZyraWebManager(http.Controller):
    @http.route('/zyra_rest_api_odoo/zyra_rest_api_odoo', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/zyra_rest_api_odoo/zyra_rest_api_odoo/objects', auth='public')
    def list(self, **kw):
        return http.request.render('zyra_rest_api_odoo.listing', {
            'root': '/zyra_rest_api_odoo/zyra_rest_api_odoo',
            'objects': http.request.env['zyra_rest_api_odoo.zyra_rest_api_odoo'].search([]),
        })

    @http.route('/zyra_rest_api_odoo/zyra_rest_api_odoo/objects/<model("zyra_rest_api_odoo.zyra_rest_api_odoo"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('zyra_rest_api_odoo.object', {
            'object': obj
        })

