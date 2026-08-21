
# Xây dựng Lớp node và Lớp Playlist manager. Khởi tạo các con trỏ head, tail, current, size. Viết hàm add_song() và is_empty()

#Khởi tạo class và con trỏ 
class Node:
    def __init__(self, ten_bai):
        self.ten = ten_bai
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def them_bai(self, ten_bai):
        new_node = Node(ten_bai)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.current = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        print("-> Da them bai hat thanh cong!")

    def next_bai(self):
        if self.current is None:
            print("-> Danh sach dang rong!")
            return
        if self.current.next is not None:
            self.current = self.current.next
            print("-> Dang phat:", self.current.ten)
        else:
            print("-> Da den bai cuoi cung roi!")

    def prev_bai(self):
        if self.current is None:
            print("-> Danh sach dang rong!")
            return
        if self.current.prev is not None:
            self.current = self.current.prev
            print("-> Dang phat:", self.current.ten)
        else:
            print("-> Dang o bai dau tien roi!")

    def xoa_bai(self, ten_bai):
        p = self.head
        while p is not None:
            # (Phải gõ chính xác hoa/thường thì mới xóa được)
            if p.ten == ten_bai: 
                if p == self.head and p == self.tail: # Có đúng 1 bài
                    self.head = None
                    self.tail = None
                    self.current = None
                elif p == self.head:
                    self.head = p.next
                    self.head.prev = None
                elif p == self.tail:
                    self.tail = p.prev
                    self.tail.next = None
                else:
                    p.prev.next = p.next
                    p.next.prev = p.prev
                # (Nếu xóa bài đang phát, con trỏ current vẫn chỉ vào bài đã xóa)

                print("-> Da xoa bai hat:", ten_bai)
                return
            p = p.next
        print("-> Khong tim thay bai hat nay trong danh sach!")

    def in_danh_sach(self):
        if self.head is None:
            print("-> Danh sach rong!")
            return
        p = self.head
        i = 1
        print("\n--- DANH SACH PHAT NHAC ---")
        while p is not None:
            if p == self.current:
                print(f"{i}. {p.ten}  <== [DANG PHAT]")
            else:
                print(f"{i}. {p.ten}")
            p = p.next
            i += 1

# --- CHƯƠNG TRÌNH CHÍNH (MENU) ---
def main():
    my_music = Playlist()
    my_music.them_bai("bai hat 1")
    my_music.them_bai("bai hat 2")
    my_music.them_bai("bai hat 3")

    while True:
        print("\n=== QUAN LY PLAYLIST ===")
        print("1. Xem danh sach bai hat")
        print("2. Them bai hat mới")
        print("3. Next (Bai tiep)")
        print("4. Prev (Bai truoc)")
        print("5. Xoa bai hat")
        print("0. Thoat")
        
        chon = int(input("Chon chuc nang (0-5): "))

        if chon == 1:
            my_music.in_danh_sach()
        elif chon == 2:
            ten = input("Nhap ten bai hat: ")
            my_music.them_bai(ten)
        elif chon == 3:
            my_music.next_bai()
        elif chon == 4:
            my_music.prev_bai()
        elif chon == 5:
            ten = input("Nhap ten bai hat can xoa: ")
            my_music.xoa_bai(ten)
        elif chon == 0:
            print("Tam biet!")
            break
        else:
            print("Loi yeu cau nhap lai! ")

if __name__ == "__main__":
    main()