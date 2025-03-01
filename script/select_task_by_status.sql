SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new');
