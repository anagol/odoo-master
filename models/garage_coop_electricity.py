from odoo import fields, models, api


class GarageCoopElectricity(models.Model):
    _name = 'garage.coop.electricity'
    _description = 'Учет электроэнергии'

    member_id = fields.Many2one('garage.coop.member', string='Член кооператива', required=True)
    garage_id = fields.Many2one('garage.coop.garage', string='Гараж', required=True)
    meter_number = fields.Char(string='Номер счетчика', required=True)
    previous_reading = fields.Float(string='Предыдущее показание')
    current_reading = fields.Float(string='Текущее показание')
    reading_date = fields.Date(string='Дата снятия показаний', default=fields.Date.today)
    consumption = fields.Float(string='Потребление (кВт·ч)', compute='_compute_consumption', store=True)
    rate = fields.Float(string='Тариф (руб/кВт·ч)', default=5.0)
    amount = fields.Float(string='Сумма к оплате', compute='_compute_amount', store=True)

    @api.depends('previous_reading', 'current_reading')
    def _compute_consumption(self):
        for record in self:
            record.consumption = record.current_reading - record.previous_reading

    @api.depends('consumption', 'rate')
    def _compute_amount(self):
        for record in self:
            record.amount = record.consumption * record.rate

    def action_create_payment(self):
        for record in self:
            self.env['garage.coop.payment'].create({
                'member_id': record.member_id.id,
                'amount': record.amount,
                'payment_type': 'electricity',
                'description': f'Оплата электроэнергии за период. Потребление: {record.consumption} кВт·ч',
            })