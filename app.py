import random
#cau truc du lieu
class Node:
    def __init__(self, title: str):
        self.title = title
        self.next = None
        self.prev = None

class PlaylistManager:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def add_song(self, title: str):
        new_node = Node(title)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.current = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def delete_song_by_title(self, title: str) -> bool:
        curr = self.head
        while curr:
            if curr.title == title:
                if curr == self.current:
                    self.current = curr.next if curr.next else curr.prev
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next

                if curr.next:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev

                self.size -= 1
                return True
            curr = curr.next
        return False

    def search_song(self, keyword: str) -> list:
        results = []
        curr = self.head
        while curr:
            if keyword.lower() in curr.title.lower():
                results.append(curr.title)
            curr = curr.next
        return results

    def shuffle_playlist(self):
        if self.size <= 1:
            return
#thu thap danh sach bai hat
        titles = []
        curr = self.head
        while curr:
            titles.append(curr.title)
            curr = curr.next

#xoa tron danh sach
        random.shuffle(titles)

#gan gia tri
        curr = self.head
        for title in titles:
            curr.title = title
            curr = curr.next
#Giao dien vs dieu khien

def get_non_empty_string(prompt: str) -> str:
    """Ngăn người dùng bỏ trống hoặc chỉ bấm Enter"""
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Loi: Du lieu khong duoc de trong! Vui long nhap lai.")

def get_valid_choice(min_choice: int, max_choice: int) -> int:
    """Ngăn lỗi nhập chữ thay vì số hoặc nhập số ngoài phạm vi Menu"""
    while True:
        try:
            choice = int(input(f"Bam chon chuc nang ({min_choice} - {max_choice}): "))
            if min_choice <= choice <= max_choice:
                return choice
            else:
                print(f"Loi: Luachon nam ngoai pham vi ({min_choice} - {max_choice}). Chon lai!")
        except ValueError:
            print("Loi: Dau vao phai la so nguyen! Vui long nhap lai.")

def display_menu(manager: PlaylistManager):
    """Hiển thị giao diện màn hình Console"""
    print("\n=============================================")
    print("      HE THONG QUAN LY MUSIC PLAYLIST        ")
    print("=============================================")
    
    current_song = manager.current.title if (manager.current and not manager.is_empty()) else "Khong co"
    print(f" Dang phat: [{current_song}]")
    print(f" Tong so bai hat: {manager.size}")
    print("---------------------------------------------")
    print("1. Them bai hat moi (Add)")
    print("2. Xoa bai hat theo ten (Delete)")
    print("3. Tim kiem bai hat (Search)")
    print("4. Phat bai ke tiep (Next)")
    print("5. Phat bai truo c do (Previous)")
    print("6. Tron bai ngau nhien (Shuffle)")
    print("7. Hien thi toan bo Danh sach phat")
    print("0. Thoat chuong trinh")
    print("=============================================")

def main_cli(manager: PlaylistManager):
    """Vòng lặp duy trì điều khiển chương trình"""
    while True:
        display_menu(manager)
        choice = get_valid_choice(0, 7)

        if choice == 1:
            print("\n--- THEM BAI HAT MOI ---")
            title = get_non_empty_string("Nhap ten bai hat: ")
            manager.add_song(title)
            print(f" Da them bai hat '{title}' vao danh sach.")

        elif choice == 2:
            print("\n--- XOA BAI HAT ---")
            if manager.is_empty():
                print(" Danh sach dang rong, khong the xoa!")
            else:
                title = get_non_empty_string("Nhap ten bai hat can xoa: ")
                if manager.delete_song_by_title(title):
                    print(f" Da xoa thanh cong bai hat '{title}'.")
                else:
                    print(f" Khong tim thay bai hat '{title}' trong danh sach.")

        elif choice == 3:
            print("\n--- TIM KIEM BAI HAT ---")
            if manager.is_empty():
                print(" Danh sach dang rong!")
            else:
                keyword = get_non_empty_string("Nhap tu khoa tim kiem: ")
                results = manager.search_song(keyword)
                if results:
                    print(f" Ket qua tim kiem cho '{keyword}':")
                    for i, song in enumerate(results, start=1):
                        print(f"   {i}. {song}")
                else:
                    print(f" Khong tim thay bai hat nao chua tu khoa '{keyword}'.")

        elif choice == 4:
            print("\n--- CHUYEN BAI KE TIEP (NEXT) ---")
            if manager.is_empty():
                print(" Danh sach rong!")
            elif manager.current and manager.current.next:
                manager.current = manager.current.next
                print(f" Dang phat: {manager.current.title}")
            else:
                print(" Da o bai hat cuoi cung trong danh sach.")

        elif choice == 5:
            print("\n--- QUAY LAI BAI TRUOC (PREVIOUS) ---")
            if manager.is_empty():
                print(" Danh sach rong!")
            elif manager.current and manager.current.prev:
                manager.current = manager.current.prev
                print(f" Dang phat: {manager.current.title}")
            else:
                print(" Da o bai hat dau tien trong danh sach.")

        elif choice == 6:
            print("\n--- TRON BAI NGAU NHIEN (SHUFFLE) ---")
            if manager.is_empty():
                print(" Danh sach rong, khong the shuffle!")
            else:
                manager.shuffle_playlist()
                print(" Da xao tron danh sach phat thanh cong!")

        elif choice == 7:
            print("\n--- TOAN BO DANH SACH PHAT ---")
            if manager.is_empty():
                print(" Danh sach hien tai dang rong!")
            else:
                curr = manager.head
                idx = 1
                while curr:
                    prefix = "-> " if curr == manager.current else "   "
                    print(f"{prefix}{idx}. {curr.title}")
                    curr = curr.next
                    idx += 1

        elif choice == 0:
            print("\n Cam on ban da su dung chuong trinh Music Playlist Manager. Tam biet!")
            break

if __name__ == "__main__":
    playlist = PlaylistManager()
    main_cli(playlist)