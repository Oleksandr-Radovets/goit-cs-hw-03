import psycopg2
from faker import Faker

host = "localhost"
port = "5432"
dbname = "mydb"
user = "sasha"
password = "sasha"

fake = Faker()

conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
)

cursor = conn.cursor()

create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(100),
        email VARCHAR(100) UNIQUE NOT NULL
    );
"""

create_status_table = """
    CREATE TABLE IF NOT EXISTS status (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL CHECK (name IN ('new', 'in progress', 'completed'))
    );
"""

create_tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100),
        description TEXT,
        status_id INTEGER REFERENCES status(id) ON DELETE CASCADE,
        user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
    );
"""

cursor.execute(create_users_table)
cursor.execute(create_status_table)
cursor.execute(create_tasks_table)
conn.commit()

statuses = ['new', 'in progress', 'completed']
for status in statuses:
    cursor.execute("INSERT INTO status (name) VALUES (%s) ON CONFLICT (name) DO NOTHING;", (status,))
conn.commit()

for _ in range(10):
    fullname = fake.name()
    email = fake.email()
    cursor.execute("INSERT INTO users (fullname, email) VALUES (%s, %s) ON CONFLICT (email) DO NOTHING;", (fullname, email))
conn.commit()


for _ in range(20):
    title = fake.sentence(nb_words=5)
    description = fake.text(max_nb_chars=200)
    status_id = fake.random_int(min=1, max=3)
    user_id = fake.random_int(min=1, max=10)
    cursor.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s);",
                   (title, description, status_id, user_id))
conn.commit()


cursor.close()
conn.close()

print("Дані успішно додано до таблиць!")

