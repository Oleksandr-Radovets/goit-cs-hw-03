SELECT users.fullname, COUNT(tasks.id)
FROM users
LEFT JOIN tasks ON users.id = tasks.user_id
GROUP BY users.fullname;