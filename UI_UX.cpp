#include "UI_UX.h"
#include <iostream>
#include <limits>

// 1. Hàm chống bỏ trống dữ liệu
std::string get_non_empty_string(const std::string &prompt)
{
    std::string input;
    while (true)
    {
        std::cout << prompt;
        std::getline(std::cin, input);

        // Loại bỏ khoảng trắng đầu/cuối
        size_t start = input.find_first_not_of(" \t\r\n");
        if (start != std::string::npos)
        {
            size_t end = input.find_last_not_of(" \t\r\n");
            return input.substr(start, end - start + 1);
        }
        std::cout << "Loi: Du lieu khong duoc de trong! Vui long nhap lai.\n";
    }
}

// 2. Hàm chống sập chương trình khi nhập sai kiểu dữ liệu/ngoại phạm vi
int get_valid_choice(int min_choice, int max_choice)
{
    int choice;
    while (true)
    {
        std::cout << "Bam chon chuc nang (" << min_choice << " - " << max_choice << "): ";
        if (std::cin >> choice)
        {
            if (choice >= min_choice && choice <= max_choice)
            {
                // Xóa bộ nhớ đệm sau khi nhập số thành công
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                return choice;
            }
            else
            {
                std::cout << "Loi: Luachon nam ngoai pham vi (" << min_choice << " - " << max_choice << "). Chon lai!\n";
            }
        }
        else
        {
            // Xử lý khi người dùng gõ chữ ("abc",...)
            std::cout << "Loi: Dau vao phai la so nguyen! Vui long nhap lai.\n";
            std::cin.clear();                                                   // Xóa cờ lỗi
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Bỏ qua dòng lỗi
        }
    }
}

// 3. Giao diện hiển thị Menu
void display_menu(PlaylistManager &manager)
{
    std::cout << "\n=============================================\n";
    std::cout << "      HE THONG QUAN LY MUSIC PLAYLIST        \n";
    std::cout << "=============================================\n";

    std::string current_song = (manager.current && !manager.is_empty()) ? manager.current->title : "Khong co";
    std::cout << " Dang phat: [" << current_song << "]\n";
    std::cout << " Tong so bai hat: " << manager.size << "\n";
    std::cout << "---------------------------------------------\n";
    std::cout << "1. Them bai hat moi (Add)\n";
    std::cout << "2. Xoa bai hat theo ten (Delete)\n";
    std::cout << "3. Tim kiem bai hat (Search)\n";
    std::cout << "4. Phat bai ke tiep (Next)\n";
    std::cout << "5. Phat bai truo c do (Previous)\n";
    std::cout << "6. Tron bai ngau nhien (Shuffle)\n";
    std::cout << "7. Hien thi toan bo Danh sach phat\n";
    std::cout << "0. Thoat chuong trinh\n";
    std::cout << "=============================================\n";
}

// 4. Vòng lặp duy trì điều khiển chương trình
void main_cli(PlaylistManager &manager)
{
    while (true)
    {
        display_menu(manager);
        int choice = get_valid_choice(0, 7);

        switch (choice)
        {
        case 1:
        {
            std::cout << "\n--- THEM BAI HAT MOI ---\n";
            std::string title = get_non_empty_string("Nhap ten bai hat: ");
            manager.add_song(title);
            std::cout << " Da them bai hat '" << title << "' vao danh sach.\n";
            break;
        }
        case 2:
        {
            std::cout << "\n--- XOA BAI HAT ---\n";
            if (manager.is_empty())
            {
                std::cout << " Danh sach dang rong, khong the xoa!\n";
            }
            else
            {
                std::string title = get_non_empty_string("Nhap ten bai hat can xoa: ");
                if (manager.delete_song_by_title(title))
                {
                    std::cout << " Da xoa thanh cong bai hat '" << title << "'.\n";
                }
                else
                {
                    std::cout << " Khong tim thay bai hat '" << title << "' trong danh sach.\n";
                }
            }
            break;
        }
        case 3:
        {
            std::cout << "\n--- TIM KIEM BAI HAT ---\n";
            if (manager.is_empty())
            {
                std::cout << " Danh sach dang rong!\n";
            }
            else
            {
                std::string keyword = get_non_empty_string("Nhap tu khoa tim kiem: ");
                auto results = manager.search_song(keyword);
                if (!results.empty())
                {
                    std::cout << " Ket qua tim kiem cho '" << keyword << "':\n";
                    for (size_t i = 0; i < results.size(); ++i)
                    {
                        std::cout << "   " << (i + 1) << ". " << results[i] << "\n";
                    }
                }
                else
                {
                    std::cout << " Khong tim thay bai hat nao chua tu khoa '" << keyword << "'.\n";
                }
            }
            break;
        }
        case 4:
        {
            std::cout << "\n--- CHUYEN BAI KE TIEP (NEXT) ---\n";
            if (manager.is_empty())
            {
                std::cout << " Danh sach rong!\n";
            }
            else if (manager.current && manager.current->next)
            {
                manager.current = manager.current->next;
                std::cout << " Dang phat: " << manager.current->title << "\n";
            }
            else
            {
                std::cout << " Da o bai hat cuoi cung trong danh sach.\n";
            }
            break;
        }
        case 5:
        {
            std::cout << "\n--- QUAY LAI BAI TRUOC (PREVIOUS) ---\n";
            if (manager.is_empty())
            {
                std::cout << " Danh sach rong!\n";
            }
            else if (manager.current && manager.current->prev)
            {
                manager.current = manager.current->prev;
                std::cout << " Dang phat: " << manager.current->title << "\n";
            }
            else
            {
                std::cout << " Da o bai hat dau tien trong danh sach.\n";
            }
            break;
        }
        case 6:
        {
            std::cout << "\n--- TRON BAI NGAU NHIEN (SHUFFLE) ---\n";
            if (manager.is_empty())
            {
                std::cout << " Danh sach rong, khong the shuffle!\n";
            }
            else
            {
                manager.shuffle_playlist();
                std::cout << " Da xao tron danh sach phat thanh cong!\n";
            }
            break;
        }
        case 7:
        {
            std::cout << "\n--- TOAN BO DANH SACH PHAT ---\n";
            if (manager.is_empty())
            {
                std::cout << " Danh sach hien tai dang rong!\n";
            }
            else
            {
                Node *curr = manager.head;
                int idx = 1;
                while (curr)
                {
                    std::string prefix = (curr == manager.current) ? "-> " : "   ";
                    std::cout << prefix << idx << ". " << curr->title << "\n";
                    curr = curr->next;
                    idx++;
                }
            }
            break;
        }
        case 0:
            std::cout << "\n Cam on ban da su dung chuong trinh Music Playlist Manager. Tam biet!\n";
            return;
        }
    }
}