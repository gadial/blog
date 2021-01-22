var Graph = function(n){
	this.n = n;
	this.E = new Array();
}

Graph.prototype = {
    add_edge: function(a,b,w){
		if (a >= this.n || b >= this.n){
			return;
		}
		if (a > b){
			this.add_edge(b,a,w);
			return;
		}
		if (this.has_edge(a,b)){
			return;
		}
		var e = [a,b];
		if ('undefined' === typeof w){
			w = Infinity;
		}
		e.w = w;
		this.E.push(e)
		return this;
    },
    has_edge: function(a,b){
		result = false;
		this.each_edge(function(e){if ((e[0] == a && e[1] == b) || (e[1] == a && e[0] == b)) result = true;})
		return result;
    },
    each_edge: function(f){
		for (var i = 0; i < this.E.length; i++){
			f(this.E[i]);
		}
    },
    find_edge: function(a,b){
		for (var i = 0; i < this.E.length; i++){
			var e = this.E[i];
			if ((e[0] == a && e[1] == b) || (e[1] == a && e[0] == b))
				return e;
		}
		return null;
    },
    remove_edge: function(a,b){
		for (var i = 0; i < this.E.length; i++){
			var e = this.E[i];
			if ((e[0] == a && e[1] == b) || (e[0] == b && e[1] == a)){
				this.E.splice(i,1);
				return;
			}
		}
	},
}

var SQUARE_SIZE = 20;
var WALL_WIDTH = 3;

var Maze = {    
    generate_raw: function(height, width){
		this.G = new Graph(height*width);
		this.height = height;
		this.width = width;
		this.cells = new Array();
		for (var y = 0 ; y < height; y++){
			for (var x = 0; x < width; x++){
				this.cells.push([x,y]);
			}
		}
		for (var y = 0 ; y < height; y++){
			for (var x = 0; x < width; x++){
				if (x > 0){
					this.G.add_edge(this.cell_index([x,y]),this.cell_index([x-1,y]),Math.random());
				}
				if (y > 0){
					this.G.add_edge(this.cell_index([x,y]),this.cell_index([x,y-1]),Math.random());
				}
			}
		}
    },
    remove_wall: function(a,b){
		this.G.remove_edge(Maze.cell_index(a),Maze.cell_index(b));
	},

	set_wall_color: function(a,b,color){
		e = Maze.G.find_edge(a,b);
		e.color = color;
    },
    draw: function(){
		Game.context.clearRect(0,0,Game.canvas.width, Game.canvas.height);
		for (var i = 0; i < this.G.E.length; i++){
			var e = this.G.E[i];
			var a = this.cells[e[0]];
			var b = this.cells[e[1]];
			this.draw_wall(a,b, e.color);
		}
		for (var x = 0; x < this.width; x++){
			this.draw_wall([x,0],[x,-1]);
			if (x != this.width-1)
				this.draw_wall([x,this.height-1],[x,this.height]);
		}
		for (var y = 0; y < this.height; y++){
			this.draw_wall([0,y],[-1,y]);
			this.draw_wall([this.width-1,y],[this.width,y]);
		}
    },
    draw_wall: function(a,b,color){
		if (a == undefined || b == undefined || (Math.abs(a[0]-b[0])+Math.abs(a[1]-b[1])) != 1){
		 return;
		}
		color = color || '#000000';
		Game.context.strokeStyle = color;
		Game.context.fillStyle = color;
		var x = WALL_WIDTH + Math.max(a[0],b[0])*(SQUARE_SIZE + WALL_WIDTH);
		var y = WALL_WIDTH + Math.max(a[1],b[1])*(SQUARE_SIZE + WALL_WIDTH);
		if (a[0] != b[0]){ //vertical wall
			Game.context.fillRect(x-WALL_WIDTH,y-WALL_WIDTH,WALL_WIDTH,SQUARE_SIZE+2*WALL_WIDTH);
		}
		if (a[1] != b[1]) { //horizontal wall
			Game.context.fillRect(x-WALL_WIDTH,y-WALL_WIDTH,SQUARE_SIZE+2*WALL_WIDTH, WALL_WIDTH);
		}
	},
}
var Game = {
    start: function(){
        Game.canvas = document.getElementById("canvas");
        Game.context = canvas.getContext('2d');
        var size = parseInt(document.getElementById("maze_size").value);
        Maze.generate_raw(size, size);
        Maze.draw();
    }
}