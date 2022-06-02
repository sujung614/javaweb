var express   = require('express');
var app       = express();
var fs        = require('fs'); 
const{PythonShell} = require('python-shell');

app.set('view engine', 'ejs'); //화면 엔진을 ejs로 설정

app.use('/', require('./routes/main'));

app.use(express.static(__dirname +'/')); //정적 파일(이미지) 제공

var port = 3000;
app.listen(port, function(){
  var dir = './uploadedFiles';
  if (!fs.existsSync(dir)) fs.mkdirSync(dir); //uploadedFiles이 존재하지 않는 경우에 생성

  console.log('server on! http://localhost:'+port);

});