from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from app.models import Vendor, Review
from app.forms import VendorForm, ReviewForm
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    vendors = Vendor.query.all()
    return render_template('index.html', vendors = vendors)
@main.route('/profile')
def profile():
    return render_template('customers/profile.html')
    
@main.route('/vendor/new', methods=['GET', 'POST'])
@login_required
def new_vendor():
    form = VendorForm()
    if form.validate_on_submit():
        vendor = Vendor(business_name=form.business_name.data, description=form.description.data, category=form.category.data, location=form.location.data, user_id=current_user.id)
        db.session.add(vendor)
        db.session.commit()
        flash('Vendor created successfully')
        return redirect(url_for('main.index'))
    return render_template('vendors/new_vendor.html', form=form)
@main.route('/vendors')
def vendors():
    vendors = Vendor.query.all()
    return render_template('vendors/new_vendor.html', vendors=vendors)

@main.route('/vendor/<int:vendor_id>')
def vendor(vendor_id):
    vendor = Vendor.query.get_or_404(vendor_id)
    reviews = Review.query.filter_by(vendor_id=vendor_id).all()
    return render_template('vendors/vendor.html', vendor=vendor, reviews=reviews)

@main.route('/vendor/<int:vendor_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_vendor(vendor_id):
    vendor = Vendor.query.get_or_404(vendor_id)
    if vendor.user_id != current_user.id:
        flash('You do not have permission to edit this vendor')
        return redirect(url_for('main.vendors'))
    form = VendorForm(obj=vendor)
    if form.validate_on_submit():
        vendor.business_name = form.business_name.data
        vendor.description = form.description.data
        vendor.category = form.category.data
        vendor.location = form.location.data
        db.session.commit()
        flash('Vendor updated successfully')
        return redirect(url_for('main.vendor', vendor_id=vendor_id))
    return render_template('vendors/edit_vendor.html', form=form)

@main.route('/vendor/<int:vendor_id>/delete', methods=['POST'])
@login_required
def delete_vendor(vendor_id):
    vendor = Vendor.query.get_or_404(vendor_id)
    if vendor.user_id != current_user.id:
        flash('You do not have permission to delete this vendor')
        return redirect(url_for('main.vendors'))
    db.session.delete(vendor)
    db.session.commit()
    flash('Vendor deleted successfully')
    return redirect(url_for('main.vendors'))

@main.route('/vendor/<int:vendor_id>/review', methods=['GET', 'POST'])
@login_required
def review_vendor(vendor_id):
    vendor = Vendor.query.get_or_404(vendor_id)
    form = ReviewForm()
    if form.validate_on_submit():
        review = Review(rating=form.rating.data, review=form.review.data, vendor_id=vendor_id, customer_id=current_user.id)
        db.session.add(review)
        db.session.commit()
        flash('Review added successfully')
        return redirect(url_for('main.vendor', vendor_id=vendor_id))
    return render_template('vendors/review_vendor.html', form=form)
