from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class VendorForm(FlaskForm):
    business_name = StringField('Business Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    category = SelectField('Category', choices=['Food', 'Services', 'Products'])
    location = StringField('Location', validators=[DataRequired()])
    submit = SubmitField('Save Changes')