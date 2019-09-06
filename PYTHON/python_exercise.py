from datetime import datetime, time


def is_prime(num):
    """
    This function takes a number as argument and checks if it is prime or not.

    Args:
        num (int): an integer number.

    Returns:
        bool: The return value. True if prime number, False otherwise.

    Examples:
        >>> is_prime(3)
        True

        >>> is_prime(4)
        False

    **Write your code below**


   """
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False

        else:
            return True
    else:
        return False

"""
Question 2: Write a Python function to convert RFC 2822 date format to ISO 8601 format.
---------------------------------------------------------------------------------------

"""


def convert_rfc2822_to_iso8601(rfcdate):
    """
    This function takes a RFC 2822 formatted date string
    and converts it to a ISO 8601 formmated date string.

    Args:
        rfcdate (str): RFC 2822 formatted date string

    Returns:
        str: The return value. ISO 8601 formatted date string

    Examples:
        >>> convert_rfc2822_to_iso8601('Fri, 21 Nov 1997 09:55:06 -0600')
        '1997-11-21T09:55:06-06:00'

        >>> convert_rfc2822_to_iso8601('Tue, 26 Jun 2018 04:00:00 UTC')
        '2018-06-26T04:00:00+00:00'

    **Write your code below**
    """
    rfcdate = rfcdate.replace('UTC', '+0000')
    offset = datetime.strptime(rfcdate, '%a, %d %b %Y %H:%M:%S %z').strftime('%z')
    return datetime.strptime(rfcdate, '%a, %d %b %Y %H:%M:%S %z').strftime('%Y-%m-%dT%H:%M:%S') + offset[:3] + ':' + offset[3:]


"""
Question 3: Write a Python class to implement Linked List.
----------------------------------------------------------

Implement a Linked List class that supports the following operations:
    * Insert: inserts a new data node into the list
    * Size: returns size of list
    * Search: searches list for a node containing the requested data and returns that node if found, otherwise raises an error
    * Delete: searches list for a node containing the requested data and removes it from list if found, otherwise raises an error
    * Generator: returns a generator that returns the next data object in the linked list

"""
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def set_data(self, new_data):
        self.data = new_data

class LinkedList(object):
    def __init__(self, head=None):
        """
        **Write your code below**
        """
        self.head = head


    def insert(self, data):
        """
        **Write your code below**
        """
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node


    def size(self):
        """
        **Write your code below**
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count


    def search(self, data):
        """
        **Write your code below**
        """
        current = self.head
        found = False
        if current.get_data() == data:
            found = True
        else:
            current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current


    def delete(self, data):
        """
        **Write your code below**
		"""
        current = self.head
        previous = None
        found = False
        if current.get_data() == data:
            found = True
        else:
            previous = current
            current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


    def generator(self):
        """
        **Write your code below**
        """
        current = self.head
        while current is not None:
            if type(current.get_data()) == int:
                if is_prime(current.get_data()):
                    self.delete(current.get_data())
            else:
                current.set_data(convert_rfc2822_to_iso8601(current.get_data()))
            current = current.get_next()



"""
Question 4: Write a Python test program using the classes and function above.
-----------------------------------------------------------------------------

Write a test program that uses all functions and LinkedList class defined in above questions.
For example, insert random numbers and RFC 2822 formatted date strings to the LinkedList,
print the initial size of the list, use the generator to convert date string to ISO format,
delete all prime numbers from the list, and print the final size of the resulted list.

Example:
    In the end, this file should be an executable Python program that can demonstrate
    all your answers to the Python programming questions listed above.::

        $ python interview_questionnaire.py

"""
from email import utils
from random import randint
import time
def main():
    # genareate random nubner
    nowdt = datetime.now()
    nowtuple = nowdt.timetuple()
    nowtimestamp = time.mktime(nowtuple)

    list = LinkedList()
    # insert random

    # insert rfc2822
    t = utils.formatdate(nowtimestamp)

    list.insert(t)
    list.insert(randint(0, 9))
    list.insert(randint(0, 9))
    list.insert(randint(0, 9))
    list.insert(randint(0, 9))
    list.insert(t)
    list.insert(randint(0, 9))
    list.insert(t)

    print('\nBefore genarator List: ')
    print_list(list)
    # print size of list
    print('\nsize of linkedlist: ')
    print(list.size())

    # Run Genarator
    print('\nRun generator')
    list.generator()

    print('\nfinal size of linkedlist: ')
    print(list.size())

    print('\nList: ')
    print_list(list)

def print_list(l):
    current = l.head
    while current is not None:
        print(current.get_data())
        current = current.get_next()

# if __name__ == "__main__":
main()