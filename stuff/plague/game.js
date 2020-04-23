WIDTH = 700;
HEIGHT = 500;
ACTOR_WIDTH = 10;
ACTOR_HEIGHT = 10;
DECAY_TIME = 100;
MAX_ACTORS = 50;
ACTORS = 30;
INFECTED = 2;
MORTALITY_RATE = 1
BIRTH_TIME = 5

LEFT_EDGE = 0;
RIGHT_EDGE = WIDTH - ACTOR_WIDTH;
LOWER_EDGE = 0;
UPPER_EDGE = HEIGHT - ACTOR_HEIGHT;

Scoreboard = {
	init: function(){
		this.healthy_count = 0;
		this.infected_count = 0;
		this.immune_count = 0;
		this.dead_count = 0;
		this.sync();
	},
	sync: function(){
		document.getElementById("healthy_count").innerHTML = this.healthy_count;
		document.getElementById("infected_count").innerHTML = this.infected_count;
		document.getElementById("immune_count").innerHTML = this.immune_count;
		document.getElementById("dead_count").innerHTML = this.dead_count;
	},
	add: function(type){
		switch(type){
			case "healthy": this.healthy_count+=1; break;
			case "infected": this.infected_count+=1; break;
			case "immune": this.immune_count+=1; break;
			case "dead": this.dead_count+=1; break;
		}
		this.sync();
	},
	remove: function(type){
		switch(type){
			case "healthy": this.healthy_count-=1; break;
			case "infected": this.infected_count-=1; break;
			case "immune": this.immune_count-=1; break;
			case "dead": this.dead_count-=1; break;
		}
		this.sync();
	}
};

Crafty.c('Actor',{
	at: function(a,b){
		this.attr({x: a,y: b});
	},
	
	moveit: function(){
		this.attr({x: this.x + this.v.x, y: this.y + this.v.y});
		if (this.x < LEFT_EDGE){
			this.x = LEFT_EDGE; this.v.x *= -1;
		}
		if (this.x > RIGHT_EDGE){
			this.x = RIGHT_EDGE; this.v.x *= -1;
		}
		if (this.y < LOWER_EDGE){
			this.y = LOWER_EDGE; this.v.y *= -1;
		}
		if (this.y > UPPER_EDGE){
			this.y = UPPER_EDGE; this.v.y *= -1;
		}
	},
	
	center_vector: function(){
		var center_x = this.x + (ACTOR_WIDTH / 2);
		var center_y = this.y + (ACTOR_HEIGHT / 2);
		return Crafty.math.Vector2D(center_x, center_y);
	},
	
	collide: function(){
//		console.log("Collide called on x=" + this.x + ", y=" + this.y);
//		console.log("Speed: " + this.v.x + ", " + this.v.y);
		var old_v = this.v;
		
		hits = this.hit("Actor");
//		console.log("Hits: " + hits);
		for (var i=0; i < hits.length; i++){
			other = hits[i].obj;
			this.v = this.v.add(hits[i].obj.v);
			old_other_v = other.v;
			
		}
		this.v.normalize();
		this.x -= old_v.x;
		this.y -= old_v.y;
	},
	
	kill: function(){
		Game.actor_count--;
		this.destroy();
	},
	
	init: function(){
		this.requires('2D, Canvas, Color, Collision');
		this.color('yellow');
		this.attr({w: ACTOR_WIDTH, h:ACTOR_HEIGHT});
		this.v = new Crafty.math.Vector2D(3,3);
		this.v.x *= (2*Crafty.math.randomInt(1,2)-3);
		this.v.y *= (2*Crafty.math.randomInt(1,2)-3);
		//this.v.normalize();
		this.bind('EnterFrame',this.moveit);
		this.onHit('Actor', function(){this.v.negate()});
		Game.actor_count++;
	},	
});

Crafty.c('Healthy',{
	infect: function(){
		if (this.has('Healthy')){
			this.addComponent('Infected'); this.removeComponent('Healthy');
			Scoreboard.remove("healthy");
		}
	},
	
	init: function(){
		this.requires('Actor');
		this.color('green');
		this.onHit('Infected', function(){this.infect()});
		Scoreboard.add("healthy");
	}
});

Crafty.c('Infected',{
	decay: function(){
		if (this.has('Infected')){
			this.life--;
			var red_value = Math.round((255*this.life) / DECAY_TIME);
			this.color('rgb(' + red_value + ', 0, 0)');
			if (this.life == 0){
				Scoreboard.remove("infected");
				if (Math.random() <= MORTALITY_RATE){
					this.kill();
					Scoreboard.add("dead");
				}
				else{
					this.addComponent('Immune'); this.removeComponent('Infected');
				}
			}
		}
	},
	
	init: function(){
		this.requires('Actor');
		this.color('red');
		this.life = DECAY_TIME;
		this.bind('EnterFrame', this.decay);
		Scoreboard.add("infected");
	}
});

Crafty.c('Immune',{
	init: function(){
		this.requires('Actor');
		this.color('blue');
		Scoreboard.add("immune");
	}
});

Game = {
	add_actor: function(){
		var a = Crafty.e('Actor');
		for (var placement_attempts = 0; placement_attempts < 10; placement_attempts++){
			a.at( Crafty.math.randomInt(0, WIDTH), Crafty.math.randomInt(0, HEIGHT));
			if (!a.hit('Actor')){
				return a;
			}
		}
		a.destroy();
		return false;
	},
	birth_tick: function(){
		Game.birth_time--;
		if (Game.birth_time == 0){
			Game.birth_time = BIRTH_TIME;
			if (Game.actor_count < MAX_ACTORS){
				var a = Game.add_actor();	
				if (a){
					a.addComponent("Healthy");
				}
			}
		}
	},
	
	start: function(){
		Scoreboard.init();
		Game.birth_time = BIRTH_TIME;
		Crafty.init(WIDTH, HEIGHT);
		Crafty.background('gray');
		
		Game.actor_count = 0;
		var Actors = new Array();
		for (var i = 0; i < ACTORS; i++){
			var a = Game.add_actor();
			if (a){
				a.addComponent("Healthy");
				Actors.push(a);
			}
			// for (var placement_attempts = 0; placement_attempts < 10; placement_attempts++){
				// a.at( Crafty.math.randomInt(0, WIDTH), Crafty.math.randomInt(0, HEIGHT));
				// if (!a.hit('Actor')){
					// break;
				// }
			// }
			// if (a.hit('Actor')){
					// a.destroy();
			// }
			// else{
				// Actors.push(a);
			// }
		}
		for (var i = 0; i < INFECTED; i++){
			Actors[i].infect();
		}
		
		// for (var i = 0; i < 1; i++){
		// Crafty.e('Infected'')
			// .at( Crafty.math.randomInt(0, 400), Crafty.math.randomInt(0, 400))
		// }
	}
}

//game_handler = Crafty.e()
//	.bind('EnterFrame',function(){
	Crafty.bind('EnterFrame',function(){
		Game.birth_tick();
});