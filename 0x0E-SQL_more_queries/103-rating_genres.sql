-- List all genres in database by their ratings
SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating FROM tv_genres JOIN tv_show_genres ON tv_genred.id = tv_show_genres.genre_id JOIN tv_show_ratings.rate ON tv_show_genres.show_id = tv_show_ratings.show_id GROUP BY tv_genres.name ORDER BY rating DESC;
