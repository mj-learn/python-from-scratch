# Create empty function
def function():
    pass  # TODO: add code later


# Create empty class
class Userr:
    pass  # TODO: add code later


# Can use pass in loops (while will go infinity), if else, function, class, method, etc ...


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Guido")
user_2 = User("002", "mOnjofn")

user_1.follow(user_2)
print(f"{user_1.username} - followers: {user_1.followers}, following: {user_1.following}")
print(f"{user_2.username} - followers: {user_2.followers}, following: {user_2.following}")
