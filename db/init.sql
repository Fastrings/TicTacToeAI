CREATE TABLE Robots (
    id serial PRIMARY KEY,
    name varchar NOT NULL
);

CREATE TABLE Results (
    ai1 int REFERENCES Robots.id NOT NULL,
    ai2 int REFERENCES Robots.id NOT NULL,
    winner int,
    draw boolean,
);

INSERT INTO Robots VALUES (1, 'random'), 
                          (2, 'get_winning'), 
                          (3, 'get_winning_and_losing'), 
                          (4, 'minimax'), 
                          (5, 'minimax2'), 
                          (6, 'mid');