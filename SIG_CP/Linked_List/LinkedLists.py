class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print(f"Inserted: {data}")

    def delete(self, data):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return

        if self.head.data == data:
            self.head = self.head.next
            print(f"Deleted: {data}")
            return

        temp = self.head
        prev = None
        while temp and temp.data != data:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found.")
            return

        prev.next = temp.next
        print(f"Deleted: {data}")

    def search(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                print(f"Found: {data}")
                return True
            temp = temp.next
        print(f"Not Found: {data}")
        return False

    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage
if __name__ == "__main__":
    ll = LinkedList()

    # Insert elements into the list
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    ll.display()  # Output: 10 -> 20 -> 30 -> None

    # Search for an element
    ll.search(20)  # Output: Found: 20
    ll.search(40)  # Output: Not Found: 40

    # Delete an element
    ll.delete(20)
    ll.display()  # Output: 10 -> 30 -> None

    # Try deleting an element not in the list
    ll.delete(40)  # Output: Value not found.
