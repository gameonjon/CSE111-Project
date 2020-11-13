-- Query 1: How many games are there for each category.
SELECT
	Games.g_genre AS Genre,
	COUNT(*) AS num
FROM
	Games
GROUP BY
	Games.g_genre
ORDER BY
	num DESC
  
-- Query 2: Sort the games based the release date.
SELECT
	Games.g_title AS Title,
	Games.g_year AS ReleaseYear
FROM
	Games
ORDER BY
	ReleaseYear ASC

-- Query 3: Display the name and corresponding developer name.
SELECT
	Games.g_title AS Title,
	Developer.d_name AS DevName
FROM
	Games,
	Developer
WHERE
	Games.g_devkey = Developer.d_devkey
ORDER BY
	DevName ASC

-- Query 4: Display all of the titles of games that were released after '2016-01-01' and are 'shooter' type games.
SELECT
    Games.g_title AS Title
FROM
    Games
WHERE
    Games.g_year > '2016-01-01'
    AND Games.g_genre = 'shooter'
ORDER BY
    Title ASC

-- Query 5: Display all games that are available on PC, Playstation 4, and Xbox One
SELECT
    Games.g_title AS Title
FROM
    Games
WHERE
    Games.g_exkey = 11
ORDER BY
    Title ASC

-- Query 6: Display all the games that are only available on a single platform. 
SELECT
    Games.g_title AS Title,
    Platform.pf_system AS System
FROM
    Games,
    Platform
WHERE
    Games.g_exkey = Platform.pf_exkey
    AND Platform.pf_exclusive = 1
ORDER BY
    Title ASC

-- Query 7: Display all games and its corresponding reviews.
SELECT
    Games.g_title AS Title,
    Reviews.r_comment AS Reviewer,
    Reviews.r_rating AS Rating,
    Reviews.r_resource AS Message
FROM
    Games,
    Reviews
WHERE
    Games.g_title = Reviews.r_gameTitle
ORDER BY
    Title ASC

-- Query 8: Display all of the publishers and the games that they worked on.
SELECT
    Publisher.p_name AS PublisherName,
    Games.g_title AS GameTitle
FROM
    Games,
    Publisher
WHERE
    Games.g_pubkey = Publisher.p_pubkey
GROUP BY
    PublisherName,
    GameTitle
ORDER BY
    PublisherName

-- Query 9: Display only the publishers that worked on more than 1 game.
SELECT
	Publisher.p_name AS PublisherName,
	Games.g_pubkey AS PublisherKey,
	COUNT(*) AS num
FROM
    Games,
    Publisher
WHERE
    Games.g_pubkey = Publisher.p_pubkey
GROUP BY
    Games.g_pubkey
HAVING
	num > 1
ORDER BY 
	PublisherName ASC

-- Query 10: List the games that were released after '2016-01-01', are 'shooter' type games, and are on Twitch.
SELECT
    Games.g_title
FROM
    Games,
    GamePlay
WHERE
    Games.g_title = GamePlay.gp_gameTitle
    AND Games.g_year > '2016-01-01'
    AND Games.g_genre = 'shooter'
    AND GamePlay.gp_platform = 'Twitch'
