import random

class Node:
    def __init__(self, title):
        self.title = title
        self.prev = None
        self.next = None
 
 
class PlaylistManager:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.size = 0
 
    def is_empty(self):
        return self.size == 0
 
    def add_song(self, title):
        new_node = Node(title)
        if self.is_empty():
            self.head = self.tail = self.current = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1
        print(f'-> Đã thêm bài hát: "{title}"')
 
    def delete_song_by_title(self, title):
        if self.is_empty():
            print("-> Danh sách rỗng, không có gì để xóa.")
            return False
 
        curr = self.head
        while curr:
            if curr.title == title:
                if self.size == 1:
                    self.head = self.tail = self.current = None
                elif curr == self.head:
                    self.head = curr.next
                    self.head.prev = None
                elif curr == self.tail:
                    self.tail = curr.prev
                    self.tail.next = None
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                self.size -= 1
                print(f'-> Đã xóa bài hát: "{title}"')
                return True
            curr = curr.next
 
        print(f'-> Không tìm thấy bài hát "{title}".')
        return False
 
    def search_song(self, keyword):
        if self.is_empty():
            print("-> Danh sách rỗng.")
            return []
        results = []
        curr = self.head
        while curr:
            if keyword.lower() in curr.title.lower():
                results.append(curr.title)
            curr = curr.next
        return results
 
    def shuffle_playlist(self):
        if self.is_empty() or self.size == 1:
            print("-> Không đủ bài hát để shuffle.")
            return
        titles = []
        curr = self.head
        while curr:
            titles.append(curr.title)
            curr = curr.next
        random.shuffle(titles)
 
        curr = self.head
        for t in titles:
            curr.title = t
            curr = curr.next
        print("-> Đã shuffle playlist!")
 
    def show_playlist(self):
        if self.is_empty():
            print("(Playlist đang trống)")
            return
        curr = self.head
        idx = 1
        while curr:
            marker = " <-- current" if curr == self.current else ""
            print(f"  {idx}. {curr.title}{marker}")
            curr = curr.next
            idx += 1
 
 
# ============================================================
# PHẦN CHÍNH - UI/UX Developer (Đình Khôi)
# ============================================================
 
def get_non_empty_string(prompt):
    """
    Ép người dùng nhập một chuỗi khác rỗng.
    Ngăn lỗi khi người dùng lỡ bấm Enter mà không gõ gì.
    """
    while True:
        value = input(prompt).strip()
        if value == "":
            print("!! Dữ liệu không được để trống. Vui lòng nhập lại.")
            continue
        return value
 
 
def get_valid_choice(prompt, min_choice, max_choice):
    """
    Ép người dùng nhập đúng một số nguyên nằm trong khoảng [min_choice, max_choice].
    Bắt cả 2 lỗi phổ biến:
      - Nhập chữ thay vì số (ValueError)
      - Nhập số ngoài phạm vi menu
    """
    while True:
        raw = input(prompt).strip()
        try:
            choice = int(raw)
        except ValueError:
            print(f'!! "{raw}" không phải là số hợp lệ. Vui lòng nhập lại.')
            continue
 
        if choice < min_choice or choice > max_choice:
            print(f"!! Vui lòng chọn số trong khoảng {min_choice}-{max_choice}.")
            continue
 
        return choice
 
 
def print_menu():
    print("\n===== MUSIC PLAYLIST MANAGER =====")
    print("1. Thêm bài hát")
    print("2. Xóa bài hát")
    print("3. Tìm kiếm bài hát")
    print("4. Shuffle playlist")
    print("5. Hiển thị playlist")
    print("0. Thoát")
 
 
def main_cli():
    playlist = PlaylistManager()
 
    while True:
        print_menu()
        choice = get_valid_choice("Nhập lựa chọn của bạn: ", 0, 5)
 
        if choice == 1:
            title = get_non_empty_string("Nhập tên bài hát cần thêm: ")
            playlist.add_song(title)
 
        elif choice == 2:
            if playlist.is_empty():
                print("-> Playlist đang rỗng, không có gì để xóa.")
            else:
                title = get_non_empty_string("Nhập tên bài hát cần xóa: ")
                playlist.delete_song_by_title(title)
 
        elif choice == 3:
            keyword = get_non_empty_string("Nhập từ khóa tìm kiếm: ")
            results = playlist.search_song(keyword)
            if results:
                print(f"-> Tìm thấy {len(results)} kết quả:")
                for r in results:
                    print(f"   - {r}")
            else:
                print("-> Không tìm thấy bài hát nào phù hợp.")
 
        elif choice == 4:
            playlist.shuffle_playlist()
 
        elif choice == 5:
            print("\n--- PLAYLIST HIỆN TẠI ---")
            playlist.show_playlist()
 
        elif choice == 0:
            print("Cảm ơn bạn đã sử dụng Music Playlist Manager. Tạm biệt!")
            break
 
 
if __name__ == "__main__":
    main_cli()
