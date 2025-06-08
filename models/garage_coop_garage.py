from odoo import models, fields, api


class GarageCoopGarage(models.Model):
    _name = 'garage.coop.garage'
    _description = 'Гараж/бокс'

    name = fields.Char(string='Номер гаража', required=True)
    size = fields.Float(string='Площадь (кв.м)')
    section = fields.Char(string='Секция/ряд')
    owner_id = fields.Many2one('garage.coop.member', string='Владелец')
    purchase_date = fields.Date(string='Дата приобретения')
    purchase_price = fields.Float(string='Стоимость приобретения')
    notes = fields.Text(string='Примечания')
    active = fields.Boolean(string='Активный', default=True)

    _sql_constraints = [
        ('garage_name_unique', 'unique(name)', 'Номер гаража должен быть уникальным!'),
    ]