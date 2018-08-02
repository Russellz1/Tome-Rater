class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def __repr__(self):
        return('User {name}, email:{email}, books read: {numOfBooks}.'
                .format(name=self.name, email = self.email, numOfBooks = len(self.books)))

    def __eq__(self, other_user):
        if self.name == other_user.name:
            if self.email == other_user.email:
                return True
        return False
    def get_email(self):
        return(self.email)

    def change_email(self, address):
        self.email = address
        print(self.name + '\'s email has changed.')

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        average = 0
        number_of_ratings = 0
        for ratings in self.books.values():
            if ratings != None:
                average += ratings
                number_of_ratings += 1
        if number_of_ratings > 0:
            return average/number_of_ratings
        else:
            return 0

class Books():
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __eq__(self, other):
        if self.title == other.title:
            if self.isbn == other.isbn:
                return True
        return False

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return(self.title)

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print(self.title + "'s isbn has been changed.")

    def add_rating(self, rating):
        if rating > 0 and rating <=4:
            self.ratings.append(rating)
        else:
            print('Invalid Rating')

    def get_average_rating(self):
        total = 0
        totalRated = 0
        for rating in self.ratings:
            if rating != None:
                total += rating
                totalRated += 1
        if totalRated > 0:
            return total/totalRated
        else:
            return 0

class Fiction(Books):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def __repr__(self):
        return '{title} by {author}'.format(title = self.title, author = self.author)

    def get_author(self):
        return self.author

class Non_Fiction(Books):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def __repr__(self):
        return ("{title}, a {level} manual on {subject}"
                .format(title = self.title, level = self.title, subject = self.subject))

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

class TombRater():

    def __init__(self):
        self.users = {}
        self.books_count = {}
        self.catalog = {}

    def check_duplicates(self, title, isbn):
        if isbn in self.catalog.values():
            print('A book with the isbn {isbn} has already been added.'.format(isbn=isbn))
            return True
        else:
            self.catalog[title] = isbn
            return False

    def create_book(self, title, isbn):
        if self.check_duplicates(title, isbn) != True:
            return Books(title, isbn)


    def create_novel(self, title, author, isbn):
        if self.check_duplicates(title, isbn) != True:
            return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        if self.check_duplicates(title, isbn) != True:
            return Non_Fiction(title, subject, level, isbn)

    def add_user(self, name, email, books = None):
        newUser = name.lower().replace(" ", "_")
        newUser = User(name, email)
        for emails in self.users.keys():
            if emails == email:
                print('There is already a user with the email address: {email}'.format(email = email))
                return
        self.users[email] = newUser
        if books != None:
            for book in books:
                newUser.read_book(book)

    def add_book_to_user(self, book, email, rating = None):
        if email in self.users.keys():
            user_key = self.users.get(email)
            user_key.read_book(book, rating)
            if rating != None:
                book.add_rating(rating)
            if book  in self.books_count.keys():
                self.books_count[book] += 1
            else:
                self.books_count[book] = 1
        else:
            print('No user with email {email}!'.format(email=email))

    def print_catalog(self):
        for book,isbn in self.catalog.items():
            print(book +  " " + str(isbn))

    def print_users(self):
        for user in self.users.values():
            print(user)

    def get_most_read_book(self):
        most_read = 0
        read_book = ""
        for book, num_of_reads in self.books_counts.items():
            if most_read < num_of_reads:
                most_read = num_of_reads
                read_book = book
        return read_book

    def highest_rated_book(self):
        highest_rating = 0
        best_book = ""
        for book in self.books_counts:
            if highest_rating < book.get_average_rating():
                highest_rating = book.get_average_rating()
                best_book = book.title
        return best_book

    def most_positive_user(self):
        highest_average = 0
        highest_user = ''
        for users in self.users.values():
            if highest_average < users.get_average_rating():
                highest_average = users.get_average_rating()
                highest_user = users
                #print(users, users.get_average_rating())
        return highest_user

