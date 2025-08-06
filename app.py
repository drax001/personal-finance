import os
from flask import Flask, render_template, redirect, url_for, request, flash
from dotenv import load_dotenv
from models import db, Transaction
from forms import TransactionForm
from services import convert_amount

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY","dev")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL","sqlite:///finance.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    @app.cli.command("init-db")
    def init_db():
        with app.app_context():
            db.create_all()
            print("DB initialized")

    @app.route("/", methods=["GET","POST"])
    def index():
        form = TransactionForm()
        if form.validate_on_submit():
            t = Transaction(
                t_type=form.t_type.data,
                category=form.category.data,
                amount=float(form.amount.data),
                currency=form.currency.data.upper(),
                note=form.note.data or ""
            )
            db.session.add(t)
            db.session.commit()
            flash("Transaction added","success")
            return redirect(url_for("index"))

        q = Transaction.query.order_by(Transaction.created_at.desc()).all()

        # quick monthly totals (server-side)
        income = sum(t.amount for t in q if t.t_type=="income")
        expense = sum(t.amount for t in q if t.t_type=="expense")
        balance = income - expense
        return render_template("index.html", form=form, items=q, income=income, expense=expense, balance=balance)

    @app.post("/delete/<int:tid>")
    def delete(tid):
        t = Transaction.query.get_or_404(tid)
        db.session.delete(t)
        db.session.commit()
        flash("Deleted","info")
        return redirect(url_for("index"))

    @app.get("/convert")
    def convert():
        amount = float(request.args.get("amount", "100"))
        frm = (request.args.get("from","USD")).upper()
        to = (request.args.get("to","CAD")).upper()
        data = convert_amount(amount, frm, to)
        flash(f"{amount} {frm} → {data['converted']:.2f} {to} (rate {data['rate']:.4f})", "secondary")
        return redirect(url_for("index"))

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
