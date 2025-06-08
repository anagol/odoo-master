from odoo import models, fields, api


class GarageCoopMember(models.Model):
    _name = 'garage.coop.member'
    _description = 'Член гаражного кооператива'
    # _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='ФИО', required=True)
    phone = fields.Char(string='Телефон')
    email = fields.Char(string='Email')
    address = fields.Text(string='Адрес проживания')
    join_date = fields.Date(string='Дата вступления', default=fields.Date.today)
    membership_number = fields.Char(string='Номер членского билета', copy=False)
    active = fields.Boolean(string='Активный', default=True)
    image = fields.Binary(string='Фото')

    garage_ids = fields.One2many('garage.coop.garage', 'owner_id', string='Гаражи')
    vehicle_ids = fields.One2many('garage.coop.vehicle', 'owner_id', string='Транспортные средства')
    payment_ids = fields.One2many('garage.coop.payment', 'member_id', string='Платежи')
    electricity_ids = fields.One2many('garage.coop.electricity', 'member_id', string='Показания электроэнергии')

    _sql_constraints = [
        ('membership_number_unique', 'unique(membership_number)', 'Номер членского билета должен быть уникальным!'),
    ]

    @api.model
    def create(self, vals):
        if not vals.get('membership_number'):
            vals['membership_number'] = self.env['ir.sequence'].next_by_code('garage_coop.member') or '/'
        return super().create(vals)