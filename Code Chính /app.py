# ==============================================================================
# FILE: app.py
# CHƯƠNG TRÌNH CHẠY MAIN MENU
# ==============================================================================

from core_struct import PlaylistManager

def main():
    playlist = PlaylistManager()

    # Nạp dữ liệu ban đầu (Đã đúng 2 tham số title, artist)
    playlist.add_song("Bai hat 1","tac gia 1")
    playlist.add_song("Bai hat 2", "Tac gia 2")
    playlist.add_song("Bai hat 3", "tac gia 3")

    while True:
        print("\n=== QUAN LY DANH SACH PHAT NHAC ===")
        if playlist.current:
            print(f" DANG PHAT: {playlist.current.title} - {playlist.current.artist}")
        else:
            print("DANG PHAT: (Danh sach rong)")

        print("-" * 35)
        print("1. Xem danh sach bai hat")
        print("2. Them bai hat moi")
        print("3. Next (Bai tiep theo)")
        print("4. Prev (Bai truoc do)")
        print("5. Xoa bai hat theo ten")
        print("6. Kiem tra toan ven lien ket (Validate)")
        print("0. Thoat")

   
        chon = int(input("Chon chuc nang (0-6): "))

        if chon == 1:
            if playlist.is_empty():
                print("-> Danh sach dang rong!")
            else:
                print(f"\n--- DANH SACH PHAT NHAC ({playlist.size} bai) ---")
                curr = playlist.head
                stt = 1
                while curr:
                    status = " <== [DANG PHAT]" if curr == playlist.current else ""
                    print(f"{stt}. {curr.title} - {curr.artist}{status}")
                    curr = curr.next
                    stt += 1

        elif chon == 2:
            ten = input("Nhap ten bai hat: ")
            casi = input("Nhap ten ca si: ")
            playlist.add_song(ten, casi)
            print("-> Da them bai hat thanh cong!")

        elif chon == 3:
            if playlist.next_song():
                print("-> Chuyen bai thanh cong!")
            else:
                print("-> Da o bai cuoi cung hoac danh sach rong!")

        elif chon == 4:
            if playlist.prev_song():
                print("-> Lui bai thanh cong!")
            else:
                print("-> Da o bai dau tien hoac danh sach rong!")

        elif chon == 5:
            ten = input("Nhap ten bai hat can xoa: ")
            if playlist.delete_song_by_title(ten):
                print("-> Da xoa thanh cong!")
            else:
                print("-> Khong tim thay bai hat!")

        elif chon == 6:
            if playlist.validate_links():
                print("-> Danh sach hop le (Head/Tail/Size chuan)!")
            else:
                print("-> Phat hien loi lien ket!")

        elif chon == 0:
            print("Tam biet!")
            break
        else:
            print("Loi: Nhap sai chuc nang, vui long nhap lai!")

if __name__ == "__main__":
    main()