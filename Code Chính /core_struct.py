# ==============================================================================
# FILE: core_struct.py
# ==============================================================================

class Node:
    def __init__(self, title: str, artist: str):

        if title == "" or artist == "":
            raise ValueError("Ten bai hat va ca si khong duoc de trong!")

        self.title = title
        self.artist = artist
        self.next = None
        self.prev = None


class PlaylistManager:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def add_song(self, title: str, artist: str):
        new_node = Node(title, artist)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.current = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.size += 1

    def next_song(self):
        if self.current and self.current.next:
            self.current = self.current.next
            return True
        return False

    def prev_song(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            return True
        return False

    def delete_song_by_title(self, title: str):
        if self.is_empty():
            return False

        curr = self.head
        while curr:

            if curr.title.lower() == title:
 
                if self.size == 1:
                    self.head = None
                    self.tail = None

                elif curr == self.head:
                    self.head = curr.next
                    self.head.prev = None
                    if self.current == curr:
                        self.current = self.head
                elif curr == self.tail:
                    self.tail = curr.prev
                    self.tail.next = None
                    if self.current == curr:
                        self.current = self.tail
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    if self.current == curr:
                        self.current = curr.next

                self.size -= 1
                return True
            curr = curr.next

        return False

    def validate_links(self):
        if self.is_empty():
            return self.head is None and self.tail is None

        # Kiểm tra con trỏ đầu và cuối
        if self.head.prev is not None or self.tail.next is not None:
            return False

        # Đếm thực tế số Node
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next

        return count == self.size