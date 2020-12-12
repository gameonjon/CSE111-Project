const sqlite3 = require('sqlite3')
const Promise = require('bluebird')


class VideoGames {
    constructor(dbFilePath) {
        this.db = new sqlite3.Database(dbFilePath, (err) => {
            if (err) {
                console.log('Could not connect to database', err)
            } else {
                console.log('Connected to database')
            }
        })
    }

    all(sql, params = []) {
        return new Promise((resolve, reject) => {
            this.db.all(sql, params, (err, rows) => {
                if (err) {
                    console.log('Error running sql: ' + sql)
                    console.log(err)
                    reject(err)
                } else {
                    resolve(rows)
                }
            })
        })
    }

    // FOR THE DROPDOWN MENU
    // ===================================================
    allGames() {
        return this.all("SELECT g_title FROM Games UNION SELECT name FROM PRAGMA_TABLE_INFO('Games') ORDER BY g_title DESC", [])
    }

    allPlatforms() {
        return this.all("SELECT pf_system FROM Platform UNION SELECT name FROM PRAGMA_TABLE_INFO('Platform') ORDER BY pf_system DESC", [])
    }

    allPublishers() {
        return this.all("SELECT p_name FROM Publisher UNION SELECT name FROM PRAGMA_TABLE_INFO('Publisher') ORDER BY p_name DESC", [])
    }

    allReviews() {
        return this.all("SELECT DISTINCT r_gameID FROM Reviews UNION SELECT name FROM PRAGMA_TABLE_INFO('Reviews') ORDER BY r_gameID DESC", [])
    }

    allContracts() {
        return this.all(
            "SELECT DISTINCT c_gameID FROM Contracts UNION SELECT name FROM PRAGMA_TABLE_INFO('Contracts') ORDER BY c_gameID DESC", [])
    }

    allDevelopers() {
        return this.all("SELECT d_name FROM Developer UNION SELECT name FROM PRAGMA_TABLE_INFO('Developer') ORDER BY d_name DESC", [])
    }

    allGamePlay() {
        return this.all(
            "SELECT DISTINCT gp_gameID FROM GamePlay UNION SELECT name FROM PRAGMA_TABLE_INFO('GamePlay') ORDER BY gp_gameID DESC", [])
    }
    // ===================================================


    // USED TO SHOW ALL OF THE DATA IN A TABLE
    // ===================================================
    showGamesTable() {
        return this.all("SELECT g_title AS Title, g_year AS Date_Released, g_genre AS Genre, g_exkey AS Available_On_Key, g_gameID AS GameID FROM Games", [])
    }

    showPlatformTable() {
        return this.all("SELECT pf_system AS Gaming_Systems, pf_exkey AS Available_On_Key, pf_exclusive AS Exclusive_Yes_No FROM Platform", [])
    }

    showPublisherTable() {
        return this.all("SELECT p_name AS Publisher_Name, p_pubkey AS Publisher_Key FROM Publisher", [])
    }

    showReviewsTable() {
        return this.all("SELECT r_gameID AS GameID, r_rating AS Rating, r_resource AS Resource, r_comment AS Comment FROM Reviews", [])
    }

    showContractsTable() {
        return this.all("SELECT c_gameID AS GameID, c_pubkey AS Publisher_Key, c_devkey AS Developer_Key FROM Contracts", [])
    }

    showDeveloperTable() {
        return this.all("SELECT d_name AS Developer_Name, d_devkey AS Developer_Key FROM Developer", [])
    }

    showGamePlayTable() {
        return this.all("SELECT gp_gameID AS GameID, gp_url AS URL, gp_platform AS Watch_On FROM GamePlay", [])
    }
    // ===================================================


}

module.exports = VideoGames
