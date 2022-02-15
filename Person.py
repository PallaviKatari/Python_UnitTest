class Person:
    name1 = []

    def set_name(self, user_name):
        self.name1.append(user_name)
        return len(self.name1) - 1

    def get_name(self, user_id):
        if user_id >= len(self.name1):
            return ' No such user Find'
        else:
            return self.name1[user_id]


if __name__ == '__main__':
    person = Person()
    print('Peter Decosta has been added with id ', person.set_name('Peter'))
    print('The user associated with id 0 is ', person.get_name(111110))