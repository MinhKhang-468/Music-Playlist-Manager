#ifndef PLAYLIST_MANAGER_H
#define PLAYLIST_MANAGER_H

#include <string>

struct Node
{
    std::string title;
    Node *next;
    Node *prev;
    Node(std::string t) : title(t), next(nullptr), prev(nullptr) {}
};

class PlaylistManager
{
public:
    Node *head = nullptr;
    Node *tail = nullptr;
    Node *current = nullptr;
    int size = 0;

    bool is_empty();
    void add_song(const std::string &title);
    bool delete_song_by_title(const std::string &title);
    std::vector<std::string> search_song(const std::string &keyword);
    void shuffle_playlist();
};

#endif