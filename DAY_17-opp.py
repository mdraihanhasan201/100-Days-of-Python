class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers=0


user1=User("001","rayhan")
user_2=User("002","tushar")


print(user1.id)
print(user1.followers)



