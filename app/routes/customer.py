from flask import render_template, redirect, url_for, flash
from app import db
from . import main
from app.models import User, Vendor
from flask_login import login_required, current_user

@main.route('/customer/profile')
@login_required
def customer_profile():
    user = User.query.get_or_404(current_user.id)
    return render_template('customers/profile.html', user=user)

@main.route('/customer/vendors')
@login_required
def customer_vendors():
    vendors = Vendor.query.all()
    return render_template('customers/vendors.html', vendors=vendors)

@main.route('/customer/vendor/<int:vendor_id>')
@login_required
def customer_vendor(vendor_id):
    vendor = Vendor.query.get_or_404(vendor_id)
    return render_template('customers/vendor.html', vendor=vendor)