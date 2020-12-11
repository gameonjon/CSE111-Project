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

    allGames() {
        return this.all(
            "SELECT g_title FROM Games", [])
    }

    allPlatforms() {
        return this.all(
            "SELECT pf_system FROM Platform", [])
    }

    allPublishers() {
        return this.all(
            "SELECT p_name FROM Publisher", [])
    }

    allReviews() {
        return this.all(
            "SELECT DISTINCT r_gameID FROM Reviews ORDER BY r_gameID ASC", [])
    }

    allContracts() {
        return this.all(
            "SELECT DISTINCT c_gameID FROM Contracts ORDER BY c_gameID ASC", [])
    }

    allDevelopers() {
        return this.all(
            "SELECT  * FROM Developer", [])
    }

    allGamePlay() {
        return this.all(
            "SELECT DISTINCT gp_gameID FROM GamePlay ORDER BY gp_gameID ASC", [])
    }

    showGamesTable() {
        return this.all("SELECT * FROM Games", [])
    }

    showPlatformTable() {
        return this.all("SELECT * FROM Platform", [])
    }

    showPublisherTable() {
        return this.all("SELECT * FROM Publisher", [])
    }

    showReviewsTable() {
        return this.all("SELECT * FROM Reviews", [])
    }

    showContractsTable() {
        return this.all("SELECT * FROM Contracts", [])
    }

    showDeveloperTable() {
        return this.all("SELECT * FROM Developer", [])
    }

    showGamePlayTable() {
        return this.all("SELECT * FROM GamePlay", [])
    }

}

module.exports = VideoGames
