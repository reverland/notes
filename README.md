<div id="wrapper"></div>
<div class="support">
	<a href="https://twitter.com/DevLoop01" target="_blank"><i class="fab fa-twitter-square"></i></a>
	<a href="https://codepen.io/dev_loop/" target="_blank"><i class="fab fa-codepen"></i></a>
</div>
<style>
  *{
	box-sizing: border-box;
	margin: 0;
	padding: 0;
}
body{
	overflow: hidden;
	background: #222;
	display: flex;
	justify-content: center;
	align-items: center;
	width: 100%;
	height: 100vh;
}


.support{
	position: fixed;
	left: 0;
	bottom: 0;
	padding: 5px;
	display: flex;
	flex-direction: column;
	background: #1abc9c;
}
a{
	margin: 5px 5px;
	color: #fff;
	font-size: 2rem;
	transition: all 400ms ease;
}

a:hover{
	color: #222;
}


</style>

<script>
class Walker{
	constructor(x, y, color){
		this.x = x;
		this.y = y;
		this.color = color;
	}
	walk(){
		var choice = floor(random(4));

		if(choice == 0){this.x++}
		else if(choice == 1){this.x--}
		else if(choice == 2){this.y++}
		else if(choice == 3){this.y--}

		this.x = constrain(this.x, width/2 - 150, width/2 + 150)
		this.y = constrain(this.y, height/2 - 150, height/2 + 150)
	}
	render(){
		stroke(this.color);
		point(this.x, this.y)
		this.walk()
	}
}


var walkers = [];
var colors = ['#FBDB4A', '#F3934A', '#EB547D', '#9F6AA7', '#70B984', '#2BB19B']
function setup(){
	var canvas = createCanvas(400, 400);
	canvas.parent('wrapper')
	background('#222');
	for(let i = 0; i < 100; i++){
		walkers.push(new Walker(random(width), random(height), colors[floor(random(colors.length))]))
	}
}

function draw(){
	walkers.forEach(walker => {
		walker.render();
	})
}

// addEventListener('resize', () => {
// 	resizeCanvas(innerWidth, innerHeight)
// })
</script>
