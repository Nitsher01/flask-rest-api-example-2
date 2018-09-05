def valid_book(book_object):
	if ('book_name' in book_object and 'book_price' in book_object and 'book_num' in book_object):
		return True
	else:
		return False