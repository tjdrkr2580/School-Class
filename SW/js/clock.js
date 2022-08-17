const tick = () => {
  var today = new Date();
  let ap;
  let h = String(today.getHours()).padStart(2, "0");
  let m = String(today.getMinutes()).padStart(2, "0");
  let dd = String(today.getDate()).padStart(2, "0");
  let mm = String(today.getMonth() + 1).padStart(2, "0");
  let ss = today.getSeconds();
  let yy = today.getFullYear();
  if (h < 13) {
    ap = "AM";
  } else {
    ap = "PM";
  }
  h -= 12;
  timeString =
    yy + "-" + mm + "-" + dd + " " + h + ":" + m + ":" + ss + " " + ap;
  document.querySelector(".clock").innerHTML = timeString;
};

setInterval(() => {
  tick();
}, 100);
