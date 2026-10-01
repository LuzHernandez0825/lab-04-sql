SELECT 
    users.username,
    users.email,
    posts.title,
    posts.body,
    posts.published_at
FROM posts
INNER JOIN users 
    ON posts.user_id = users.user_id
WHERE posts.user_id IN (1, 2, 7)
ORDER BY posts.post_id ASC;
