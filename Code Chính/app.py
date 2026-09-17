from flask import Flask, render_template, request, jsonify
from core_struct import PlaylistManager

app = Flask(__name__)
playlist = PlaylistManager()

# Init some default songs
playlist.add_song("Bật Tình Yêu Lên", "Hòa Minzy, Tăng Duy Tân")
playlist.add_song("Waiting For You", "MONO, Onionn")
playlist.add_song("Em Đồng Ý (I Do)", "Đức Phúc, 911")

def get_playlist_data():
    songs = []
    curr = playlist.head
    current_title = playlist.current.title if playlist.current else None
    
    idx = 1
    while curr:
        songs.append({
            "id": idx,
            "title": curr.title,
            "artist": curr.artist,
            "is_current": curr == playlist.current
        })
        curr = curr.next
        idx += 1
    
    return {
        "songs": songs,
        "current": current_title,
        "size": playlist.size
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/playlist", methods=["GET"])
def api_playlist():
    return jsonify(get_playlist_data())

@app.route("/api/add", methods=["POST"])
def api_add():
    data = request.json
    title = data.get("title", "").strip()
    artist = data.get("artist", "").strip()
    if not title or not artist:
        return jsonify({"success": False, "error": "Title and artist are required"}), 400
    
    try:
        playlist.add_song(title, artist)
        return jsonify({"success": True, "data": get_playlist_data()})
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400

@app.route("/api/next", methods=["POST"])
def api_next():
    playlist.next_song()
    return jsonify({"success": True, "data": get_playlist_data()})

@app.route("/api/prev", methods=["POST"])
def api_prev():
    playlist.prev_song()
    return jsonify({"success": True, "data": get_playlist_data()})

@app.route("/api/delete", methods=["POST"])
def api_delete():
    data = request.json
    title = data.get("title", "")
    success = playlist.delete_song_by_title(title)
    if success:
        return jsonify({"success": True, "data": get_playlist_data()})
    return jsonify({"success": False, "error": "Song not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)