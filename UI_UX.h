#ifndef UI_UX.h
#define UI_UX .h

#include "PlaylistManager.h"
#include <string>

// Ngăn người dùng bỏ trống hoặc chỉ bấm Enter
std::string get_non_empty_string(const std::string &prompt);

// Ngăn lỗi nhập chữ thay vì số hoặc nhập số ngoài phạm vi Menu
int get_valid_choice(int min_choice, int max_choice);

// Hiển thị giao diện màn hình Console
void display_menu(PlaylistManager &manager);

// Vòng lặp duy trì Menu chính
void main_cli(PlaylistManager &manager);

#endif