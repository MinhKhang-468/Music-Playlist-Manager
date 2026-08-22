
import random

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
                    if self.head:
                        self.head.prev = None
                elif p == self.tail:
                    self.tail = p.prev
                    if self.tail:
                        self.tail.next = None
                else:
                    p.prev.next = p.next
                    p.next.prev = p.prev
                # (Nếu xóa bài đang phát, con trỏ current vẫn chỉ vào bài đã xóa)

                print("-> Da xoa bai hat:", ten_bai)
                return
            p = p.next
        print("-> Khong tim thay bai hat nay trong danh sach!")

    def delete_song_by_title(self, ten_bai):
        if self.head is None:
            print("-> Danh sach dang rong!")
            return

        p = self.head
        while p is not None:
            if p.ten == ten_bai: 
                # Xử lý cập nhật current nếu bài hát bị xóa là bài đang phát
                if self.current == p:
                    if p.next is not None:
                        self.current = p.next
                    else:
                        self.current = p.prev

                # Xử lý các trường hợp xóa
                if p == self.head and p == self.tail: # Có đúng 1 bài
                    self.head = None
                    self.tail = None
                elif p == self.head: # Xóa bài đầu tiên
                    self.head = p.next
                    if self.head:
                        self.head.prev = None
                elif p == self.tail: # Xóa bài cuối cùng
                    self.tail = p.prev
                    if self.tail:
                        self.tail.next = None
                else: # Xóa bài ở giữa
                    p.prev.next = p.next
                    p.next.prev = p.prev

                print("-> Da xoa bai hat:", ten_bai)
                return
            p = p.next
            
        print("-> Khong tim thay bai hat nay trong danh sach!")

    def search_song(self, ten_bai):
        if self.head is None:
            print("-> Danh sach rong!")
            return None
        
        p = self.head
        vi_tri = 1
        while p is not None:
            if p.ten == ten_bai:
                print(f"-> Tim thay '{ten_bai}' tai vi tri so {vi_tri}.")
                return p
            p = p.next
            vi_tri += 1
            
        print(f"-> Khong tim thay '{ten_bai}' trong danh sach.")
        return None

    def shuffle_playlist(self):
        if self.head is None or self.head == self.tail:
            print("-> Khong du bai hat de xao tron!")
            return
            
        # Đưa các node vào danh sách để xáo trộn
        nodes = []
        p = self.head
        while p is not None:
            nodes.append(p)
            p = p.next
            
        # Xáo trộn danh sách
        random.shuffle(nodes)
        
        # Xây dựng lại các liên kết
        self.head = nodes[0]
        self.tail = nodes[-1]
        
        for i in range(len(nodes)):
            nodes[i].prev = nodes[i - 1] if i > 0 else None
            nodes[i].next = nodes[i + 1] if i < len(nodes) - 1 else None
            
        print("-> Da xao tron danh sach phat thanh cong!")

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
        print("5. Xoa bai hat (Code cu)")
        print("6. Xoa bai hat (Yeu cau moi)")
        print("7. Tim kiem bai hat")
        print("8. Xao tron danh sach")
        print("0. Thoat")
        
        chon = int(input("Chon chuc nang (0-8): "))

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
            ten = input("Nhap ten bai hat can xoa (Cu): ")
            my_music.xoa_bai(ten)
        elif chon == 6:
            ten = input("Nhap ten bai hat can xoa (Moi): ")
            my_music.delete_song_by_title(ten)
        elif chon == 7:
            ten = input("Nhap ten bai hat can tim: ")
            my_music.search_song(ten)
        elif chon == 8:
            my_music.shuffle_playlist()
        elif chon == 0:
            print("Tam biet!")
            break
        else:
            print("Loi yeu cau nhap lai! ")

if __name__ == "__main__":
    main()