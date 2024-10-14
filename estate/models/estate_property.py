# -*- coding: utf-8 -*-

from odoo import models, fields
from dateutil.relativedelta import relativedelta


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Property'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Available From', copy=False, default=lambda self: fields.Date.today() + relativedelta(months=3))
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price', readonly=True, copy=False)
    bedrooms = fields.Integer(string='Bedrooms', default=2)
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area (sqm)')
    garden_orientation = fields.Selection([('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')], string='Garden Orientation')
    active = fields.Boolean(string='Active', default=True)
    state = fields.Selection([('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')], string='State', required=True, copy=False, default='new')
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    partner_id = fields.Many2one('res.partner', string='Buyer')
    user_id = fields.Many2one('res.users', string='Salesman', default=lambda self: self.env.user)


class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Property Type'

    name = fields.Char(string='Name', required=True)
