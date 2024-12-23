DROP TABLE IF EXISTS image_gallery;


CREATE TABLE image_gallery (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);