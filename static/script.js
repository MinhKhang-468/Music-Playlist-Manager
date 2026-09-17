document.addEventListener("DOMContentLoaded", () => {
    fetchPlaylist();

    document.getElementById("btn-next").addEventListener("click", () => {
        postData("/api/next", {}).then(updateUI);
    });

    document.getElementById("btn-prev").addEventListener("click", () => {
        postData("/api/prev", {}).then(updateUI);
    });

    // We can simulate Play/Pause visual
    const playBtn = document.getElementById("btn-play");
    playBtn.addEventListener("click", () => {
        const icon = playBtn.querySelector("i");
        if(icon.classList.contains("fa-play")) {
            icon.classList.remove("fa-play");
            icon.classList.add("fa-pause");
        } else {
            icon.classList.remove("fa-pause");
            icon.classList.add("fa-play");
        }
    });

    document.getElementById("add-song-form").addEventListener("submit", (e) => {
        e.preventDefault();
        const titleInput = document.getElementById("input-title");
        const artistInput = document.getElementById("input-artist");
        
        const payload = {
            title: titleInput.value,
            artist: artistInput.value
        };

        postData("/api/add", payload).then(res => {
            if(res.success) {
                updateUI(res);
                titleInput.value = "";
                artistInput.value = "";
            } else {
                alert(res.error || "Failed to add song.");
            }
        });
    });
});

function fetchPlaylist() {
    fetch("/api/playlist")
        .then(res => res.json())
        .then(data => updateUI({data: data}))
        .catch(err => console.error(err));
}

async function postData(url = "", data = {}) {
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });
    return response.json();
}

function deleteSong(title) {
    postData("/api/delete", {title: title}).then(updateUI);
}

function updateUI(response) {
    if(!response || !response.data) return;
    const data = response.data;
    
    // Update player info
    const currentTitleEl = document.getElementById("current-title");
    const currentArtistEl = document.getElementById("current-artist");
    
    // Find current song details
    const currentSong = data.songs.find(s => s.is_current);
    
    if(currentSong) {
        currentTitleEl.textContent = currentSong.title;
        currentArtistEl.textContent = currentSong.artist;
    } else {
        currentTitleEl.textContent = "Not Playing";
        currentArtistEl.textContent = "Playlist is empty";
    }

    // Update count
    document.getElementById("song-count").textContent = `${data.size} songs`;

    // Render list
    const ul = document.getElementById("playlist-ul");
    ul.innerHTML = "";

    data.songs.forEach((song, index) => {
        const li = document.createElement("li");
        li.className = `song-item ${song.is_current ? 'active' : ''}`;
        li.style.animationDelay = `${index * 0.05}s`;
        
        li.innerHTML = `
            <div class="song-info">
                <span class="song-title">${song.title}</span>
                <span class="song-artist">${song.artist}</span>
            </div>
            <button class="delete-btn" onclick="deleteSong('${song.title.replace(/'/g, "\\'")}')" title="Delete">
                <i class="fas fa-trash-alt"></i>
            </button>
        `;
        
        ul.appendChild(li);
    });
}
