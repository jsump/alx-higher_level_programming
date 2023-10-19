-- List all genres and dispay the number of shows linke to each
SELECT tv_genres.genre AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows FROM tv_genres JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY tv_genres.genre ORDER BY number_of_shows DESC;
