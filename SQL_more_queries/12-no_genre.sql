-- Command The only SELECT statement that displays all shows that do not have an associated genre. To achieve this, a LEFT JOIN is used between tv_shows and tv_show_genres, filtering out cases where gene_id is NULL.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
