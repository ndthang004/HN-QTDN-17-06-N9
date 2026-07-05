from odoo import models, fields


class KhachHang(models.Model):
    _name = 'quanlykhachhang.khachhang'
    _description = 'Khach Hang'

    ma_khach_hang = fields.Char(
        string='Mã khách hàng',
        required=True
    )

    ten_khach_hang = fields.Char(
        string='Tên khách hàng',
        required=True
    )

    so_dien_thoai = fields.Char(
        string='Số điện thoại'
    )

    email = fields.Char(
        string='Email'
    )

    dia_chi = fields.Text(
        string='Địa chỉ'
    )

    nhan_vien_phu_trach = fields.Many2one(
        'hr.employee',
        string='Nhân viên phụ trách'
    )

    van_ban_ids = fields.One2many(
        'quanlykhachhang.vanban',
        'khach_hang_id',
        string='Hồ sơ số hóa'
    )