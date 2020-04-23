// var DynamicData = function(){this.}
// DynamicData.prototype = {
	// hello: function(){console.log("hello world!")},
	// static_arr: [1,2,3]
// }

var init = function(){
	$('input').keyup(calculate_and_draw);
	calculate_and_draw();
}

var calculate_and_draw = function(){
	var S_0 = parseInt($('#S_0')[0].value);
	var I_0 = parseInt($('#I_0')[0].value);
	var BETA = parseInt($('#BETA')[0].value)/(S_0*I_0);
	var ALPHA = parseInt($('#ALPHA')[0].value)/I_0;
	var GAMMA = parseInt($('#GAMMA')[0].value);
	var STEPS = parseInt($('#STEPS')[0].value);
	var S_e = [[0,ALPHA / BETA]];
	var S = [[0,S_0]];
	var I = [[0,I_0]];
	for (var n = 1; n < STEPS; n++){
		var S_p = S[n-1][1];
		var I_p = I[n-1][1];
		var delta = BETA * S_p * I_p
		var grow = (n % GAMMA == 0)?(5):(0);
		S.push([n, S_p - delta + grow]);
		I.push([n, I_p + delta - I_p*ALPHA]);
		S_e.push([n,ALPHA/BETA]);
	}
	
	var data = [
		{ data: S, label: 'S' },
		{ data: I, label: 'I'},
		{ data: S_e, label: 'S_e'}
	];

	var options = {
		canvas: true,
		xaxes: [ { min: 0 } ],
		yaxes: [ { min: 0 }, {
			position: 'right',
			alignTicksWithAxis: 1,			
		} ],
		legend: { position: 'nw' }
	}

	$.plot('#placeholder', data, options);
};

$(document).ready(init);
// a = new DynamicData();
// b = new DynamicData();

// console.log(a.static_arr);
// console.log(b.static_arr);
// a.static_arr[0] = 17;
// console.log(a.static_arr);
// console.log(b.static_arr);

