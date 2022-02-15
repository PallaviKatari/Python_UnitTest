import unittest

# First we import the class which we want to test.
import Person as PerClass


class Test(unittest.TestCase):
    """
    The basic class that inherits unittest.TestCase
    """
    person = PerClass.Person()  # instantiate the Person Class
    user_id = []  # This variable stores the obtained user_id
    user_name = []  # This variable stores the person name

    # It is a test case function to check the Person.set_name function
    def test_0_set_name(self):
        print("Start set_name test\n")

        for i in range(4):
            # initialize a name
            name = 'name' + str(i)
            # put the name into the list variable
            self.user_name.append(name)
            # extraxt the user id obtained from the function
            user_id = self.person.set_name(name)
            # check if the obtained user id is null or not
            self.assertIsNotNone(user_id)
            # store the user id to the list
            self.user_id.append(user_id)
        print("The length of user_id is = ", len(self.user_id))
        print(self.user_id)
        print("The length of user_name is = ", len(self.user_name))
        print(self.user_name)
        print("\nFinish set_name test\n")

        # Second test case function to check the Person.get_name function

    # def test_1_get_name(self):
    #     print("\nStart get_name test\n")
    #
    #     # total number of stored user information
    #     length = len(self.user_id)
    #     print("The length of user_id is = ", length)
    #     print("The lenght of user_name is = ", len(self.user_name))
    #     for i in range(6):
    #         # if i not exceed total length then verify the returned name
    #         if i < length:
    #             # if the two name not matches it will fail the test case
    #             self.assertEqual(self.user_name[i], self.person.get_name(self.user_id[i]))
    #         else:
    #             print("Testing for get_name no user test")
    #             # if length exceeds then check the 'no such user' type message
    #             self.assertEqual('There is no such user', self.person.get_name(i))
    #     print("\nFinish get_name test\n")


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()