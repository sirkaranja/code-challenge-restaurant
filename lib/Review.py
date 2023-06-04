from sqlalchemy import String, Integer, Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///review.db')
Base = declarative_base
Session = sessionmaker(bind=engine)
session = Session()

class Review(Base):
    __tablename__ ='reviews'

    review_id = Column(Integer, primary_key = True)
    restaurant= Column(String)
    restaurant_customer= Column(String)
    customer_rating= Column(Integer)


    all_reviews= []
    def __init__(self, restaurant,restaurant_customer, customer_rating):
        self.restaurant = restaurant
        self.restaurant_customer = restaurant_customer
        self.customer_rating = customer_rating
        Review.all_reviews.append(self)

    def rating(self):
        return self.customer_rating
    
    @classmethod
    def all(cls):
        for review in cls.all_reviews:
            return review


