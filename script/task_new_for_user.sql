INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('New Task', 'This is a new task description', (SELECT id FROM status WHERE name = 'new'), 1);