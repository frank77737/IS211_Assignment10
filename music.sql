CREATE TABLE artist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL -- Artist name
);

CREATE TABLE album (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, -- Album name
    artist_id INTEGER NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artist(id) -- Artist ID
);

CREATE TABLE song (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT NOT NULL, -- Song name
    album_id INTEGER NOT NULL,
    track_number INTEGER NOT NULL,
    length_seconds INTEGER NOT NULL,
    FOREIGN KEY (album_id) REFERENCES album(id) -- Album ID
);

