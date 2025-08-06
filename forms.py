from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Length

class TransactionForm(FlaskForm):
    t_type = SelectField("Type", choices=[("expense","Expense"),("income","Income")], validators=[DataRequired()])
    category = StringField("Category", validators=[DataRequired(), Length(max=50)])
    amount = DecimalField("Amount", places=2, validators=[DataRequired()])
    currency = StringField("Currency", default="USD", validators=[DataRequired(), Length(max=5)])
    note = StringField("Note", validators=[Length(max=255)])
    submit = SubmitField("Add")
