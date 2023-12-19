CREATE TABLE IF NOT EXISTS Player (
    id INTEGER AUTO_INCREMENT,
    username varchar(20),
    wins INTEGER,
    losses INTEGER,
    primary key (id)
);

-- INSERT INTO Player(username, wins, losses)
-- VALUES ("bentheduster", 3, 0)