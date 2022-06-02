var express  = require('express');
var router   = express.Router();
var multer   = require('multer');
var mysql = require('mysql');
var fs        = require('fs');
const app = express();
const{PythonShell} = require('python-shell');

var storage  = multer.diskStorage({
  destination(req, file, cb) {
    cb(null, 'uploadedFiles/');
  },
  filename(req, file, cb) {
    cb(null, `${file.originalname}`);
  },
});
var uploadWithOriginalFilename = multer({ storage: storage });

router.get('/', function(req,res){
  res.render('upload');
});

router.post('/uploadFileWithOriginalFilename', uploadWithOriginalFilename.single('attachment'), function(req,res){
  res.render('confirmation', { file:req.file, files:null });

app.get('/uploadFileWithOriginalFilename', function(req,res){
  res.status(200).sendFile(__dirname + '/confirmation.ejs')
});

const sql = fs.readFileSync('./routes/makeDB.sql').toString();

let connection = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "0614",
  multipleStatements: true
});

connection.connect(function(err) {
  if (err) throw err;
  
  connection.query(sql, function (err, result) {
    if (err) throw err;
    console.log("Database created");
  });
});

fs.readFile('./uploadedFiles/inputFile.txt', 'utf8', (err, data)=>{
    if(err) throw err;    else {
        let line = data.split('\r\n');      let mix = [];
        line.forEach((value, index) => {mix[index] = value.split('\t');})
        mix.splice(6,1);
        mix.splice(12,1);
        mix.splice(18,1);
        mix.splice(24,1);
        mix.splice(30,1);
        mix.splice(36,1);
        mix.splice(42,1);
        mix.splice(48,1);
        mix.splice(54,1);
        mix.splice(60,1);
        connection.query('truncate `inputfile`;')
        mix.forEach((value, index)=>{
          connection.query('INSERT INTO `inputfile` (col1, col2, col3, col4, col5, col6) VALUES(?, ?, ?, ?, ?, ?);', value, (error, results, fields)=>{
              if (error) throw error;        else console.log(`파일의 데이터가 삽입되었습니다.`);    });});
    }
});
let options = {
  scriptPath: "./javawebreport",
};
PythonShell.run("report.py", options, function(err, data) {
  if (err) throw err;
});
});

module.exports = router;