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

var Maze = {
    ...
    }