from bookstore import db

class Book(db.Document):
 	"""docstring for Book"""
 	__tablename__ = 'books'
 	
 	book_name = db.StringField(100)
 	book_price = db.FloatField()
 	book_num = db.IntField()
 	
 	def __repr__(self):
 		return f"""book_name: {self.book_name},
book_price: {self.book_price},
book_num: {self.book_num}
 		"""
