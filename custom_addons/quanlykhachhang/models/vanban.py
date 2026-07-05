from odoo import models, fields

class VanBan(models.Model):
    _name = 'quanlykhachhang.vanban'
    _description = 'Van Ban'

    ma_van_ban = fields.Char(
        string='Mã văn bản'
    )

    ten_van_ban = fields.Char(
        string='Tên văn bản',
        required=True
    )

    khach_hang_id = fields.Many2one(
        'quanlykhachhang.khachhang',
        string='Khách hàng'
    )
    
    loai_van_ban = fields.Selection([
        ('hopdong', 'Hợp đồng'),
        ('baogia', 'Báo giá'),
        ('phaply', 'Tài liệu pháp lý'),
        ('bienban', 'Biên bản'),
        ('khac', 'Khác')
    ], string='Loại văn bản')

    ngay_tao = fields.Date(
        string='Ngày tạo'
    )

    tep_dinh_kem = fields.Binary(
        string='Tệp đính kèm'
    )

    ten_tep = fields.Char(
        string='Tên file'
    )
    
    ghi_chu = fields.Text(
        string='Ghi chú'
    )