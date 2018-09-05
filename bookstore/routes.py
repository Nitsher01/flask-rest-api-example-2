from bookstore import app, db
from flask import  jsonify, request, Response,redirect, url_for
from utils import valid_book
from bookstore.models import Book

@app.route('/books',methods=['GET','POST'])
def get_all_books():
	books = []
	if request.method == 'GET':
		print('THis is get request')
		for book in Book.query.all():
			temp_dict = {
				'book_name': book.book_name,
				'book_price': book.book_price,
				'book_num' : book.book_num
			}
			books.insert(0, temp_dict)
		return jsonify(books)
	elif request.method == 'POST':
		print('This is post request', request.get_json())
		request_data = request.get_json()
		if valid_book(request_data):
			new_book = Book(book_name = request_data['book_name'], book_price = request_data['book_price'], book_num = request_data['book_num'])
			new_book.save()
			books.append(request.get_json())
			response = Response("",201,mimetype = "application/json") # 201 response i.e created 
			response.headers['Location'] = '/books/'+str(request_data['book_num']) # link in the header
			redirect(url_for('get_all_books'))
			return response
		return Response("",400,mimetype = "application/json")


@app.route('/books/<int:book_num>')
def get_book(book_num):
	book = Book.query.filter_by(book_num = book_num).first()
	if book:
		return jsonify({
			'book_name': book.book_name,
			'book_price': book.book_price,
			'book_num' : book.book_num
			})
	return Response("",400,mimetype = "application/json")


@app.route('/books/<int:book_num>',methods=['PUT']) # replace/ put new object in place of old object
def replace_book(book_num):
	request_data = request.get_json()
	print('Replace book', request_data)
	if valid_book(request_data):
		book = Book.query.filter_by(book_num = book_num).first()
		# print('Inside valid book', book)
		if book:
			book.book_name = request_data['book_name']
			book.book_price = request_data['book_price']
			book.save()
			return Response("",201,mimetype="application/json")
	return Response("",400,mimetype = "application/json")


@app.route('/books/<int:book_num>',methods=['PATCH']) # patch for updating some informations instead of replacing whole object
def update_book(book_num):
	print('Update book')
	request_data = request.get_json()
	if valid_book(request_data):
		book = Book.query.filter_by(book_num = book_num).first()
		if book:
			if 'book_name' in request_data:
				book.book_name = request_data['book_name']
			if 'book_price' in request_data:
				book.book_price = request_data['book_price']
			book.save()
			return Response("",201,mimetype="application/json")
	return Response("",400,mimetype = "application/json")


@app.route('/books/<int:book_num>',methods=['DELETE']) # delete the book 
def delete_book(book_num):
	book = Book.query.filter_by(book_num = book_num).first()
	if book:
		book.remove()
		return Response("",201,mimetype = "application/json")
	return Response("",400,mimetype = "application/json")

@app.route('/')
def index():
	return jsonify({'Hello World': 'Just this'})
