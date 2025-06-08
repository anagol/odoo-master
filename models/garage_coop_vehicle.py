from odoo import fields, models, api


class GarageCoopVehicle(models.Model):
    _name = 'garage.coop.vehicle'
    _description = 'Транспортное средство'

    license_plate = fields.Char(string='Гос. номер', required=True)
    make = fields.Char(string='Марка')
    model = fields.Char(string='Модель')
    year = fields.Integer(string='Год выпуска')
    color = fields.Char(string='Цвет')
    vin = fields.Char(string='VIN-код')
    owner_id = fields.Many2one('garage.coop.member', string='Владелец', required=True)
    garage_id = fields.Many2one('garage.coop.garage', string='Прикрепленный гараж')
    notes = fields.Text(string='Примечания')

    _sql_constraints = [
        ('license_plate_unique', 'unique(license_plate)', 'Гос. номер должен быть уникальным!'),
    ]