from odoo import models, fields

class VanBan(models.Model):
    _name = 'van_ban'
    _description = 'Quản lý văn bản'

    so_van_ban = fields.Char(
        string='Số văn bản',
        required=True
    )

    tieu_de = fields.Char(
        string='Tiêu đề',
        required=True
    )

    ngay_tao = fields.Date(
        string='Ngày tạo',
        default=fields.Date.today
    )

    loai_van_ban = fields.Selection([
        ('hop_dong', 'Hợp đồng'),
        ('bao_gia', 'Báo giá'),
        ('phap_ly', 'Tài liệu pháp lý'),
        ('cong_van', 'Công văn')
    ], string='Loại văn bản')

    trang_thai = fields.Selection([
        ('draft', 'Nháp'),
        ('processing', 'Đang xử lý'),
        ('done', 'Hoàn thành')
    ], default='draft')
