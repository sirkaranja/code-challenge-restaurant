from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()



#class Customer(populates the table customer)
class Customer(Base):
    #declared table name and its attributes 
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    given_name = Column(String)
    family_name = Column(String)
    reviews = relationship('Review', back_populates='customer')

    #method to return full name by concatinating given name and family name
    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    #method to give a review based on the restaurant 
    def add_review(self, restaurant, rating):
        review = Review(customer=self, restaurant=restaurant, rating=rating)
        self.reviews.append(review)

    def restaurants(self):
        return [review.restaurant for review in self.reviews]
    #method to return the number of reviews given by a particular user.
    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, name):
        session = Session()
        customer = session.query(cls).filter(cls.full_name() == name).first()
        session.close()
        return customer

    @classmethod
    def find_all_by_given_name(cls, given_name):
        session = Session()
        customers = session.query(cls).filter(cls.given_name == given_name).all()
        session.close()
        return customers



#class Restaurant, populates the restaurant table
class Restaurant(Base):
      #declared table name and its attributes 
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    reviews = relationship('Review', back_populates='restaurant')


    def __init__(self, name):
        self.name = name

    #method to return the average rating
    def average_star_rating(self):
        total_ratings = sum(review.rating for review in self.reviews)
        num_reviews = len(self.reviews)
        if num_reviews == 0:
            return 0
        return total_ratings / num_reviews

    def customers(self):
        return [review.customer for review in self.reviews]


#class review, populates the table review
class Review(Base):

      #declared table name and its attributes 
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    rating = Column(Integer)
    customer = relationship('Customer', back_populates='reviews')
    restaurant = relationship('Restaurant', back_populates='reviews')


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


engine = create_engine('sqlite:///hospitality.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)









