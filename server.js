// Create express app
var express = require("express")
var app = express()


const VideoGames = require("./videogames")
var project = new VideoGames('data.sqlite')

// Server port
var HTTP_PORT = 8092

app.use(function (req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');
    res.setHeader('Access-Control-Allow-Credentials', true);

    next();
});

// Start server
app.listen(HTTP_PORT, () => {
    console.log("Server running on port %PORT%".replace("%PORT%", HTTP_PORT))
});

// Root endpoint
app.get("/", (req, res, next) => {
    res.json({ "message": "Ok" })
});


//                  ONLY TOUCH STUFF BELOW THIS POINT!!!
// ======================================================================

// Games table
app.get("/api/games", (req, res, next) => {
    project.allGames()
        .then((makers) => {
            res.json({
                "message": "success",
                "data": makers
            })
        })
        .catch((err) => {
            res.status(400).json({ "error": err.message });
            return;
        })
});

// Platforms table
app.get("/api/platforms", (req, res, next) => {
    project.allPlatforms()
        .then((makers) => {
            res.json({
                "message": "success",
                "data": makers
            })
        })
        .catch((err) => {
            res.status(400).json({ "error": err.message });
            return;
        })
});


// Default response for any other request
app.use(function (req, res) {
    res.status(404);
});
// ======================================================================
