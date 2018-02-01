var x, y; //wspolrzedne obiektow
var flag;
function setup() {
  createCanvas(600,600);
  background(200);
  frameRate(60);

}

function draw() {

  noFill();
  noStroke();

  if(mouseIsPressed){
    if(mouseButton===LEFT){
    fill('red');
    strokeWeight(20);
    stroke('yellow');
  };
  if(mouseButton===CENTER){
  fill(200);
  strokeWeight(30);
  stroke(200);
  rect(mouseX-10, mouseY-10, 20, 20);
};

  }

    point(mouseX,mouseY);









}
