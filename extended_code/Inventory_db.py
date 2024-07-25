from sqlalchemy import create_engine, Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import Numeric


engine = create_engine("sqlite:///Inventory.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Product(Base):
    __tablename__ = "Products"

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String)
    product_quantity = Column(Integer)
    product_price = Column(Numeric(10, 2))
    date_updated = Column(Date)

    def __repr__(self):
        return f"""id: {self.product_id}
                \rname: {self.product_name}
                \rquantity: {self.product_quantity}
                \rprice: {self.product_price}
                \rupdated: {self.date_updated}"""


if __name__ == "__main__":
    Base.metadata.create_all(engine)
