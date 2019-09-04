function _() {
let CSS = `
#_horloge {
	position: fixed;
	width: 200px;
	height: 200px;
	background: rgba(14,118,211,0.5);
	border: 1px solid rgb(14,118,211);
	border-radius: 50%;
	cursor: grab;
	z-index: 10000000;
}

#_horloge:active {
	cursor: grabbing;
}

#_horloge_canvas {
	position: absolute;
	top: 4px;
	left: 4px;
	width: calc(100% - 8px);
	height: calc(100% - 8px);
	background: #eee;
	border-radius: 50%;
	pointer-events: none;
}
`;

let HTML = `
<div id="_horloge" style="top: 0; left: 0;">
	<canvas id="_horloge_canvas"></canvas>
</div>
`;

let REGEX = /(-?\d+)(?:px)/;

let CTX = null;

function ajouterPx(coord, ajout) {
	let base = parseInt(REGEX.exec(coord)[1]);
	return (base + ajout) + "px";
}

function dessinHorloge() {
	CTX.clearRect(0, 0, 192, 192);
	dessinCadran(CTX);
	dessinAiguilles(CTX);
	window.requestAnimationFrame(dessinHorloge);
}

function dessinCadran(ctx) {
	ctx.beginPath();
	ctx.strokeStyle="#000000";
	ctx.lineWidth=1;
	for (let i = 0; i < 12; i++)
	{
		ctx.moveTo(96 + Math.cos(i * 2 * Math.PI / 12)*96,96 + Math.sin(i * 2 * Math.PI / 12)*96);
		ctx.lineTo(96 + Math.cos(i * 2 * Math.PI / 12)*90,96 + Math.sin(i * 2 * Math.PI / 12)*90);
	}
	for (let i = 0; i < 60; i++)
	{
		ctx.moveTo(96 + Math.cos(i * 2 * Math.PI / 60)*96,96 + Math.sin(i * 2 * Math.PI / 60)*96);
		ctx.lineTo(96 + Math.cos(i * 2 * Math.PI / 60)*94,96 + Math.sin(i * 2 * Math.PI / 60)*94);
	}
	ctx.stroke();
}

function dessinAiguilles(ctx) {
	let date = new Date();
	let angle = null;

	ctx.beginPath();
	let sec = date.getSeconds();
	angle = sec * 2 * Math.PI / 60 - Math.PI / 2;
	ctx.strokeStyle="#DD0000";
	ctx.lineWidth=1;
	ctx.moveTo(96,96);
	ctx.lineTo(96 + Math.cos(angle) * 84, 96 + Math.sin(angle) * 84);
	ctx.stroke();

	ctx.beginPath();
	let min = date.getMinutes() + sec / 60;
	angle = min * 2 * Math.PI / 60 - Math.PI / 2;
	ctx.strokeStyle="#000000";
	ctx.lineWidth=2;
	ctx.moveTo(96,96);
	ctx.lineTo(96 + Math.cos(min) * 74, 96 + Math.sin(min) * 74);
	ctx.stroke();

	ctx.beginPath();
	let heure = date.getHours() % 12 + min / 60;
	angle = heure * 2 * Math.PI / 12 - Math.PI / 2;
	ctx.strokeStyle="#000000";
	ctx.lineWidth=3;
	ctx.moveTo(96,96);
	ctx.lineTo(96 + Math.cos(angle) * 64, 96 + Math.sin(angle) * 64);
	ctx.stroke();
}

document.head.insertAdjacentHTML("beforeend","<style>"+CSS+"</style>");
document.body.insertAdjacentHTML("beforeend", HTML);

let popup = document.getElementById("_horloge");
let canvas = document.getElementById("_horloge_canvas");

popup.addEventListener("mousedown", e => popup.classList.add("drag"));
document.addEventListener("mouseup", e => popup.classList.remove("drag"));
document.addEventListener("mousemove", e => {
	if (popup.classList.contains("drag"))
	{
		popup.style.top = ajouterPx(popup.style.top, e.movementY);
		popup.style.left = ajouterPx(popup.style.left, e.movementX);
	}
});

canvas.width = canvas.clientWidth;
canvas.height = canvas.clientHeight;
CTX = canvas.getContext('2d');
window.requestAnimationFrame(dessinHorloge);
}; _();
