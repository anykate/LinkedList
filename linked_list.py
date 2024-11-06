from dataclasses import dataclass


@dataclass
class Node:
    data: int
    next: int = None


@dataclass
class LinkedList:
    head: Node = None

    def insert_at_end(self, data: int) -> None:
        node = Node(data)

        if not self.head:
            self.head = node
            # print(f'Inserting at beginning of linked list: {data}')
            return

        last = self.head

        while last.next:
            last = last.next

        last.next = node
        # print(f'Inserting at end of linked list: {data}')
        return

    def display(self) -> None:
        if not self.head:
            print('List is empty')
            return

        current = self.head

        while current:
            if current.next:
                print(current.data, ' -> ', end='')
            else:
                print(current.data, '.', sep='')

            current = current.next

    def search(self, data: int) -> None:
        if not self.head:
            print('List is empty')
            return

        current = self.head

        while current:
            if current.data == data:
                print(f'Element found: {current.data}')
                return

            current = current.next

        print('Element not found')


if __name__ == '__main__':
    ll = LinkedList()

    while True:
        try:
            print("\n")
            print("1) Add data to Linked List")
            print("2) Display Linked List")
            print("3) Search data in Linked List")
            print("\nEnter any numeric value to terminate the program...")

            choice = int(input('Enter your choice: '))

            match choice:
                case 1:
                    ele = int(input('Enter element to add: '))
                    ll.insert_at_end(ele)

                case 2:
                    ll.display()

                case 3:
                    ele = int(input('Enter element to be searched for: '))
                    ll.search(ele)

                case _:
                    print('Terminating...')
                    break

        except ValueError:
            print("Invalid input")
