SELECT tasks.*
FROM tasks
JOIN users ON tasks.user_id = users.id
WHERE users.email LIKE '%@example.com';