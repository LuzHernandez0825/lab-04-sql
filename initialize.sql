DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE posts (
    post_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(150) NOT NULL,
    body TEXT NOT NULL,
    published_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_posts_users
        FOREIGN KEY (user_id) 
        REFERENCES users(user_id)
        ON DELETE CASCADE
);

INSERT INTO users (username, email) VALUES
('alex_mitchells', 'alexm@virginia.edu'),
('sarah_paul', 'sarahp@virginia.edu'),
('jordan_peele', 'jordanp@virginia.edu'),
('taylor_swift', 'taylors@virginia.edu'),
('morgan_furgeson', 'morganf@virginia.edu'),
('casey_might', 'caseym@virginia.edu'),
('riley_wright', 'rileyw@virginia.edu'),
('reagan_evans', 'reagane@virginia.edu'),
('christopher_combs', 'christopherc@virginia.edu'),
('jennie_yang', 'jenniey@virginia.edu');

INSERT INTO posts (user_id, title, body) VALUES
(1, 'Getting Started with SQL', 'SQL scripts allow you to automate database builds easily.'),
(1, 'Understanding Database Keys', 'Primary and Foreign keys ensure data integrity across tables.'),
(2, 'My Favorite Python Frameworks', 'Flask and FastAPI are great lightweight options.'),
(3, 'Designing REST APIs', 'Good API design relies on consistent endpoints and HTTP verbs.'),
(5, 'Intro to Git & GitHub', 'Version controlling your SQL files prevents loss of work.'),
(6, 'Digital Illustration Tips', 'Color balance and composition bring digital art to life.'),
(7, 'Overcoming Writer’s Block', 'Writing a rough draft first helps momentum.'),
(7, 'Structuring a Short Story', 'Focus on setup, central tension, and resolution.'),
(10, 'Data Normalization 101', 'Structuring databases efficiently avoids redundant data.'),
(2, 'Building Full-Stack Apps', 'Connecting frontend frameworks to robust SQL backends.');
