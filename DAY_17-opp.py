class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers=0
        self.following=0


    def follow (self,user):
        user.followers+=1
        user.following+=1


user1=User("001","rayhan")
user_2=User("002","tushar")
user1.follow(user_2)

print(user1.followers)
print(user_2.followers)
print(user1.following)
print(user_2.following)











