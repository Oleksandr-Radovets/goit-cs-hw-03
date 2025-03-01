SELECT status.name, COUNT(tasks.id)
FROM status
LEFT JOIN tasks ON status.id = tasks.status_id
GROUP BY status.name;