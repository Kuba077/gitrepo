var lenghth=30;
x=y=100;
function setup() {
  createCanvas(600,600);
  background(200);
  // frameRate(120);

}

function draw() {
background(200);
dx=mouseX-x;
dy=mouseY-y;

angle1=atan2(dy,dx);
x=mouseX-(cos(angle1)*lenghth);
y=mouseY-(sin(angle1)*lenghth);
rect(x,y,30,30);









}
