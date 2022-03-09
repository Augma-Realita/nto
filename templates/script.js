var vid = document.getElementById("videoel");
var vid_width = vid.width;
var vid_height = vid.height;
var overlay = document.getElementById("overlay");

var overlayCC = overlay.getContext("2d");
var bird = new Image();
var pipeUp = new Image(); // Создание объекта
var pipeBottom = new Image();
var gap = 90;
var score = 0;
var pipe = []
var p = 20



pipe[0] = {
  x : overlay.width,
  y : 0
}


/*********** Setup of video/webcam and checking for webGL support *********/
function enablestart() {
  var startbutton = document.getElementById("startbutton");
  startbutton.value = "start";
  startbutton.disabled = null;
}

var insertAltVideo = function (video) {
  // insert alternate video if getUserMedia not available
  if (supports_video()) {
    if (supports_webm_video()) {
      video.src = "./media/cap12_edit.webm";
    } else if (supports_h264_baseline_video()) {
      video.src = "./media/cap12_edit.mp4";
    } else {
      return false;
    }
    return true;
  } else return false;
};

function adjustVideoProportions() {
  // resize overlay and video if proportions of video are not 4:3
  // keep same height, just change width
  var proportion = vid.videoWidth / vid.videoHeight;
  vid_width = Math.round(vid_height * proportion);
  vid.width = vid_width;
  overlay.width = vid_width;
}

function gumSuccess(stream) {
  // add camera stream if getUserMedia succeeded
  if ("srcObject" in vid) {
    vid.srcObject = stream;
  } else {
    vid.src = window.URL && window.URL.createObjectURL(stream);
  }
  vid.onloadedmetadata = function () {
    adjustVideoProportions();
    vid.play();
  };
  vid.onresize = function () {
    adjustVideoProportions();
    if (trackingStarted) {
      ctrack.stop();
      ctrack.reset();
      ctrack.start(vid);
    }
  };
}

function gumFail() {
  // fall back to video if getUserMedia failed
  insertAltVideo(vid);
  document.getElementById("gum").className = "hide";
  document.getElementById("nogum").className = "nohide";
  alert(
    "There was some problem trying to fetch video from your webcam, using a fallback video instead."
  );
}
navigator.getUserMedia =
  navigator.getUserMedia ||
  navigator.webkitGetUserMedia ||
  navigator.mozGetUserMedia ||
  navigator.msGetUserMedia;
window.URL = window.URL || window.webkitURL || window.msURL || window.mozURL;
// set up video
if (navigator.mediaDevices) {
  navigator.mediaDevices
    .getUserMedia({ video: true })
    .then(gumSuccess)
    .catch(gumFail);
} else if (navigator.getUserMedia) {
  navigator.getUserMedia({ video: true }, gumSuccess, gumFail);
} else {
  insertAltVideo(vid);
  document.getElementById("gum").className = "hide";
  document.getElementById("nogum").className = "nohide";
  alert(
    "Your browser does not seem to support getUserMedia, using a fallback video instead."
  );
}
vid.addEventListener("canplay", enablestart, false);

/*********** Code for face tracking *********/
var ctrack = new clm.tracker();
ctrack.init();
var trackingStarted = false;

vid.play();
// start tracking
ctrack.start(vid);
trackingStarted = true;
// start loop to draw face
drawLoop();

pipeUp.src = "../static/pipeUp.png"; // Аналогично
pipeBottom.src = "../static/pipeBottom.png";

function drawLoop() {
  bird.src = "../static/bird.png";

  requestAnimFrame(drawLoop);
  overlayCC.clearRect(0, 0, vid_width, vid_height);

  if (ctrack.getCurrentPosition()) {
    // get points
    var positions = ctrack.getCurrentPosition();
    var pupilLeft = positions[37]
    for(var i = 0; i < pipe.length; i++) {
      overlayCC.drawImage(pipeUp, pipe[i].x + p, pipe[i].y);
      overlayCC.drawImage(pipeBottom, pipe[i].x + p, pipe[i].y + pipeUp.height + gap);
      pipe[i].x--;

      if(pipe[i].x == 125){
        pipe.push({
          x : overlay.width,
          y : Math.floor((Math.random() * pipeUp.height) - pipeUp.height)
        })
      }
      if(pupilLeft[0] + bird.width >= pipe[i].x && pupilLeft[0] <= pipe[i].x + pipeUp.width &&
          (pupilLeft[1] <= pipe[i].y + pipeUp.height || pupilLeft[1] + bird.height >= pipe[i].y + pipeUp.height + gap)){
        location.reload();
      }
      if(pipe[i].x == 180){

        score++;
      }
    }



    // draw circles over eyes
    overlayCC.fillStyle = "#000";

    overlayCC.beginPath();
    overlayCC.drawImage(bird ,pupilLeft[0] - 17, pupilLeft[1] - 17);

    overlayCC.closePath();
    overlayCC.fill();
    overlayCC.font = "24px Verdana";
    overlayCC.fillText( "Счет: " + score, 10, overlay.height - 20);
  }
}

