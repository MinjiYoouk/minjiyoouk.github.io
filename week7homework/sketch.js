let shapes = ['triangle', 'circle', 'square'];
let exampleShape;
let randomShapeLoop;
let button;
let intervalId;

function setup() {
  createCanvas(600, 600);
  background(255);
  setupGame();
  drawGame();
  intervalId = setInterval(changeRandomShape, 1000);
}

function setupGame() {
  exampleShape = random(shapes);
  randomShapeLoop = random(shapes);
  
  if (button) {
    button.remove();
  }
  button = createButton('Press');
  button.style('width', '150px');  
  button.style('height', '50px');  
  button.position(width / 2 - button.width / 2, 500);
  button.mousePressed(checkShapes);
}

function drawGame() {
  background(255);
  drawShape(exampleShape, width / 2, 100);
  drawShape(randomShapeLoop, width / 2, 300);
}

function drawShape(shape, x, y) {
  if (shape === 'triangle') {
    fill(0, 0, 255);
    triangle(x - 30, y + 30, x + 30, y + 30, x, y - 30);
  } else if (shape === 'circle') {
    fill(255, 0, 0);
    ellipse(x, y, 60, 60);
  } else if (shape === 'square') {
    fill(0, 128, 0);
    rectMode(CENTER);
    rect(x, y, 60, 60);
  }
}

function changeRandomShape() {
  randomShapeLoop = random(shapes);
  drawGame();
}

function checkShapes() {
  clearInterval(intervalId);
  
  if (exampleShape === randomShapeLoop) {
    background(0, 255, 0); // Green for success
    button.html('Success!!!');
  } else {
    background(255, 0, 0); // Red for failure
    button.html('Fail!!!');
  }

  drawShape(exampleShape, width / 2, 100);
  drawShape(randomShapeLoop, width / 2, 300);
  
  setTimeout(() => {
    setupGame();
    drawGame();
    intervalId = setInterval(changeRandomShape, 1000);
  }, 2000);
}

