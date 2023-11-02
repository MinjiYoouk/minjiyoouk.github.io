let shapes = ['smiley', 'frowning', 'faceless'];
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
  button.style('font-size', '22px'); // font size

  
   // Set the button's base color to light blue
  button.style('background-color', '#537DF9');
  button.style('border', 'none');
  button.style('color', 'white'); 
  
    // Add hover effect
  button.mouseOver(function() {
  button.style('background-color', '#537DF9');  // Hover color
  });
  button.mouseOut(function() {
  button.style('background-color', '#212634');  // Base color
  });
  
  button.position(width / 2 - button.width / 2, 500);
  button.mousePressed(checkShapes);
}

function drawGame() {
  background(255);
  drawShape(exampleShape, width / 2, 100);
  drawShape(randomShapeLoop, width / 2, 300);
}
function drawShape(shape, x, y) {
  if (shape === 'smiley') {
    fill(255, 255, 0);  // Yellow
    ellipse(x, y, 60, 60); // Face
    fill(0); // Black for eyes
    ellipse(x - 12, y - 8, 8, 8); // Left eye
    ellipse(x + 12, y - 8, 8, 8); // Right eye
    noFill();
    arc(x, y + 5, 30, 20, 0, PI, CHORD); // Smiling mouth
  } 
  else if (shape === 'frowning') {
    fill(255, 0, 0);  // Red
    ellipse(x, y, 60, 60); // Face
    fill(0); // Black for eyes
    ellipse(x - 12, y - 8, 8, 8); // Left eye
    ellipse(x + 12, y - 8, 8, 8); // Right eye
    noFill();
    arc(x, y + 15, 30, 20, PI, TWO_PI, CHORD); // Frowning mouth
  } 
  else if (shape === 'faceless') {
    fill(0);  // Black
    ellipse(x, y, 60, 60); // Face
    fill(255);  // White for eyes and mouth
    ellipse(x - 12, y - 8, 8, 8); // Left eye
    ellipse(x + 12, y - 8, 8, 8); // Right eye
    line(x - 20, y + 15, x + 20, y + 15); // Straight mouth
  }
}


function changeRandomShape() {
  randomShapeLoop = random(shapes);
  drawGame();
}

function checkShapes() {
  clearInterval(intervalId);
  
  if (exampleShape === randomShapeLoop) {
    button.html('Success!!!');
    button.style('background-color', 'rgb(0, 208, 32)'); // Change button color to green on success
    background(0, 255, 0); // Green for success
  } else {
    button.html('Fail!!!');
    button.style('background-color', 'rgb(200, 0, 0)'); // Change button color to red on failure
    background(255, 0, 0); // Red for failure
  }

  drawShape(exampleShape, width / 2, 100);
  drawShape(randomShapeLoop, width / 2, 300);
  
  setTimeout(() => {
    setupGame();
    drawGame();
    intervalId = setInterval(changeRandomShape, 500);
  }, 2000);
}

