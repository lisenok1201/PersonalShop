from sqlalchemy import DECIMAL, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.base import Base
from .users import Users


class Carts(Base):
    __tablename__ = "carts"
    id: Mapped[int] = mapped_column(primary_key=True)
    total_price: Mapped[int] = mapped_column(DECIMAL(10, 2), default=0)
    total_products: Mapped[int] = mapped_column(default=0)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)

    user_cart: Mapped["Users"] = relationship(back_populates="carts")
    finally_id: Mapped[int] = relationship("FinallyCarts", back_populates="user_cart")


    def __str__(self):
        return str(self.id)


class FinallyCarts(Base):# Объявляет модель FinallyCarts, наследующуюся от Base.
    __tablename__ = "finally_carts"# Устанавливает имя таблицы в базе данных: "finally_carts".
    id: Mapped[int] = mapped_column(primary_key=True)# Колонка 'id': целочисленный первичный ключ.
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))# Колонка 'product_id': вторичный ключ, ссылающийся на 'products.id'.
    product_name: Mapped[str] = mapped_column(String(50))# Колонка 'product_name': строка до 50 символов (имя продукта).
    final_price: Mapped[DECIMAL] = mapped_column(DECIMAL(10, 2))# Колонка 'final_price': десятичное число (цена), 10 цифр всего, 2 после запятой.
    quantity: Mapped[int]# Колонка 'quantity': целочисленное значение (количество).

    cart_id: Mapped[int] = mapped_column(ForeignKey("carts.id"))# Колонка 'cart_id': вторичный ключ, ссылающийся на 'carts.id'.
    user_cart: Mapped[Carts] = relationship(back_populates="finally_id")# Отношение 'user_cart' к модели Carts, связывающееся через 'finally_id' в Carts.

    table_args = (
        {'sqlite_autoincrement': True},# Для SQLite: автоматический инкремент первичного ключа. Инкремент-операция, увеличивающая значение переменной.
    )


    def __str__(self):
        return str(self.id)