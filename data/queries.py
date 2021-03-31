from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT * FROM shows;')


def save_users(email, password):
    data_manager.execute_dml_statement(
        "INSERT INTO users(email, password, role) VALUES('"+email+"','"+password+"','user');")


def list_users(email, password):
    return data_manager.execute_select(
        "SELECT email, password, role FROM users WHERE email LIKE '"+email+"' AND password LIKE '"+password+"' ")


def get_show(id):
    return data_manager.execute_select('SELECT * FROM shows WHERE id=' + id + ';')


def top_shows(page_number):
    return data_manager.execute_select("""
    SELECT json_agg(t)
    FROM (
    SELECT (shows.id) as id,title,year,rating,trailer,homepage,runtime,ARRAY_AGG (name) genres
FROM shows 
INNER JOIN show_genres ON (shows.id = show_genres.show_id)
INNER JOIN genres ON (show_genres.genre_id = genres.id)
GROUP BY shows.id,title,year,rating,trailer,homepage,runtime
ORDER BY
    shows.rating DESC
LIMIT
    15
OFFSET (%(Page_number)s -1)*15) t
    """, variables={"Page_number": page_number})
