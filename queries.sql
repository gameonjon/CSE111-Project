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

-- Q11: Insert into gameplay
INSERT INTO GamePlay (gp_gameTitle, gp_url, gp_platform)
    VALUES ("Spider-Man", "https://www.youtube.com/results?search_query=spider+man+2018", "Twitch");

-- Q12: Insert into Games
INSERT INTO Games (g_title, g_year, g_genre, g_exkey, g_pubkey, g_devkey)
    VALUES ("The Last of Us Part II", "2020-06-19", "survival-horror", 1, 10005, 20025);

-- Q13: Insert into Reviews
INSERT INTO Reviews (r_gameTitle, r_rating, r_resource, r_comment)
    VALUES ("The Last of Us Part II", 10, "Unkown", "The Last of Us Part II is messy, bleak, and brutal.");

-- Q14: Update Reviews
UPDATE Reviews
    SET r_rating = 8, r_resource = "GameSpot"
    WHERE r_gameTitle = "The Last of Us Part II";

-- Q15: Delete Review by Metro GameCentral
DELETE FROM Reviews
    WHERE r_resource = "Metro GameCentral";

-- Q16: Update Gamplay spider-man to platfomr youtube
UPDATE GamePlay
    SET gp_platform = "Youtube"
    WHERE gp_gameTitle = "Spider-Man";

-- Q17: Select the reviews from games whos publisher is "Sony Interactive Entertainment"
SELECT *
    FROM Reviews, Games, Publisher
    WHERE p_name = "Sony Interactive Entertainment" AND
        g_pubkey = p_pubkey
    GROUP BY r_resource;

-- Q18: select the develper with publisher "Sony Interactive Entertainment"
SELECT d_name
    FROM Games, Developer, Publisher
    WHERE p_name = "Sony Interactive Entertainment" AND
        g_pubkey = p_pubkey AND
        d_devkey = g_devkey
    GROUP BY d_name;

-- Q19: get game title, system, and publisher for exclusively made games
SELECT g_title, pf_system, p_name
    FROM Platform, Games, Publisher
    WHERE pf_exclusive = 1 AND
        g_exkey = pf_exkey AND
        g_pubkey = p_pubkey;

-- Q20: delete ratings 8.9 and lower
DELETE FROM Reviews
    WHERE r_rating < 9;
