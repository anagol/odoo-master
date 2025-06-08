from odoo import fields, models, api


class GarageCoopPayment(models.Model):
    _name = 'garage.coop.payment'
    _description = 'Членские взносы'
    # _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Номер платежа', readonly=True, default='New')
    member_id = fields.Many2one('garage.coop.member', string='Член кооператива', required=True)
    date = fields.Date(string='Дата платежа', default=fields.Date.today)
    amount = fields.Float(string='Сумма', required=True)
    payment_type = fields.Selection([
        ('membership', 'Членский взнос'),
        ('electricity', 'Оплата электроэнергии'),
        ('fine', 'Штраф'),
        ('other', 'Прочее'),
    ], string='Тип платежа', required=True, default='membership')
    description = fields.Text(string='Назначение платежа')
    state = fields.Selection([
        ('draft', 'Черновик'),
        ('posted', 'Проведен'),
        ('cancelled', 'Отменен'),
    ], string='Статус', default='draft')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('garage.coop.payment') or 'New'
        return super().create(vals)

    def action_post(self):
        self.write({'state': 'posted'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})