// Drawing functions in canvas
let initDrawingPt = false;
let prevMouseX = 0;
let currMouseX = 0;
let prevMouseY = 0;
let currMouseY = 0;
let lineWidth = 3;
let color = "orange";


function startGestureMouse(canvas, e) {
  let ctx = canvas.getContext("2d");
  // clear canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  prevMouseX = currMouseX;
  prevMouseY = currMouseY;
  currMouseX = e.clientX - canvas.offsetLeft;
  currMouseY = e.clientY - canvas.offsetTop;
  
  // initDrawingPt = true;
  // if (initDrawingPt) {
    ctx.beginPath();
    ctx.fillStyle = color;
    ctx.arc(currMouseX, currMouseY, 5, 0, Math.PI * 2, true);
    ctx.fill();
    ctx.closePath();
    initDrawingPt = false;
  // }
}

function startGestureTouch(canvas, e) {
  mousePos = getTouchPos(canvas, e);
  var touch = e.touches[0];
  var mouseEvent = new MouseEvent("mousedown", {
      clientX: touch.clientX,
      clientY: touch.clientY
  });
  canvas.dispatchEvent(mouseEvent);
}

// Get the position of a touch relative to the canvas
function getTouchPos(canvasDom, touchEvent) {
  var rect = canvasDom.getBoundingClientRect();
  return {
    x: touchEvent.touches[0].clientX - rect.left,
    y: touchEvent.touches[0].clientY - rect.top
  };
}

function drawGestureMouse(canvas, e) {
  let ctx = canvas.getContext("2d");
  prevMouseX = currMouseX;
  prevMouseY = currMouseY;
  currMouseX = e.clientX - canvas.offsetLeft;
  currMouseY = e.clientY - canvas.offsetTop;
  ctx.beginPath();
  ctx.moveTo(prevMouseX, prevMouseY);
  ctx.lineTo(currMouseX, currMouseY);
  ctx.strokeStyle = color;
  ctx.lineWidth = lineWidth; 
  ctx.stroke();
  ctx.closePath();
  
}


function drawGestureTouch(canvas, e) {
  var touch = e.touches[0];
  var mouseEvent = new MouseEvent("mousemove", {
    clientX: touch.clientX,
    clientY: touch.clientY
  });
  //document.getElementById('dataset-div').innerHTML = touch.clientX.toString() + ' / ' + touch.clientY.toString();
  canvas.dispatchEvent(mouseEvent);
}

function addGestureThumbnail(canvas, gesture_id) {
    // declare the canva where to draw a thumbnail
    let thumbCnvs = document.createElement('canvas');
    thumbCnvs.width = 70;
    thumbCnvs.height = 70;
    thumbCnvs.style.border = "1px solid";
    // get context to fill with bkg color and image
    let ctx = thumbCnvs.getContext('2d');
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, thumbCnvs.width, thumbCnvs.height); 
    ctx.drawImage(canvas, 0, 0, canvas.width, canvas.height, 0, 0, thumbCnvs.width, thumbCnvs.height);
    // add to the body document
    var body = document.getElementsByTagName("body")[0];
    body.appendChild(thumbCnvs);
}


function getMouseXYinCanvas(canvas, e) {
  const { top, left, width, height } = canvas.getBoundingClientRect();
  const clientX = (e.pageX - left) / width;
  const clientY = (e.pageY - top) / height;
  return [clientX, clientY]
}


function addBoxToBody(width, height, name, boxtitle) {
  // create outer DIV
  var iDiv = document.createElement('div');
  iDiv.id = 'block-'+String(Math.random() * 10000);
  iDiv.className = 'box';
  document.getElementsByTagName('body')[0].appendChild(iDiv);
  // create canvas
  let canvas = document.createElement('canvas');
  canvas.width = width;
  canvas.height = height;
  canvas.style.border = "0px";
  canvas.id = name;
  let ctx = canvas.getContext('2d');
  ctx.fillStyle = "white";
  ctx.fillRect(0, 0, canvas.width, canvas.height); 
  let div = document.getElementById(iDiv.id);
  div.appendChild(canvas);
  // create div for title
  let titleDiv = document.createElement('div');
  titleDiv.className = 'boxtitle';
  titleDiv.innerHTML += boxtitle;
  div.appendChild(titleDiv);
}


export { addBoxToBody, drawGestureMouse, drawGestureTouch, startGestureMouse, startGestureTouch, addGestureThumbnail, getMouseXYinCanvas };
