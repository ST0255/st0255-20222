const express = require("express");
var path = require('path');
const app = express();
const PORT = 8080;

app.use('/static/css', express.static(path.join(__dirname, '../public/css/')))
app.use('/static/img', express.static(path.join(__dirname, '../public/img/')))

app.use(express.urlencoded({extended: true}));

app.listen(PORT, () => {
 console.log('Server is running on port: ' + PORT);
});

app.get('/', function (req, res) {

    var indexFile = path.join(__dirname, '../public', 'index.html');
    res.sendFile(indexFile)
});


app.post('/form',function(req, res){

    var userFirstName = req.body.firstname;
    var userLastName = req.body.lastname;
    var userCountry = req.body.country;
    var userComments = req.body.subject;

    var answerFile = path.join(__dirname, '../public', 'answer.html');
    res.sendFile(answerFile)
});

