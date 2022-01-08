//var DIR = "/stuff/Nim/"
var DIR = "/assets/img/other/nim/"
var GAME = {};

function setCookie(c_name,value,exdays){
	var exdate=new Date();
	exdate.setDate(exdate.getDate() + exdays);
	var c_value=escape(value) + ((exdays==null) ? "" : "; expires="+exdate.toUTCString());
	document.cookie=c_name + "=" + c_value;
}

function getCookie(c_name){
	var i,x,y,ARRcookies=document.cookie.split(";");
	for (i=0;i<ARRcookies.length;i++){
		x=ARRcookies[i].substr(0,ARRcookies[i].indexOf("="));
		y=ARRcookies[i].substr(ARRcookies[i].indexOf("=")+1);
		x=x.replace(/^\s+|\s+$/g,"");
		if (x==c_name){
			return unescape(y);
		}
	}
}

var rand = function(n){
	return Math.floor((Math.random()*n)); 
}

var display_message = function(talker_pic, msg_txt){
	$("#speaker_image")[0].setAttribute('src', talker_pic);
	$("#speaker_image")[0].style.display = 'hidden'
	$("#speaker_text")[0].innerHTML = msg_txt;
}

var remove_message = function(){
	$("#speaker_image")[0].style.display = 'inline'
	$("#speaker_image")[0].setAttribute('src', "");
	$("#speaker_text")[0].innerHTML = "";
}


var new_row_element = function(row,length){
	var element = document.createElement('tr');
	for (var i=0; i < length; i++){
		var o = document.createElement('img');
		o.setAttribute('src', DIR + 'mushroom.jpg');
		var cell = document.createElement('td');
		cell.appendChild(o);
		cell.num = i;
		cell.onclick = function(){
			GAME.remove_from_row(row,this.num);
		};		
		element.appendChild(cell)
	}
	return element;
}

var init = function() {
	GAME.randomize_board = function(min_rows, max_rows, min_cols, max_cols){
		this.board = new Array();
		var rows = min_rows + rand(max_rows + 1 -min_rows);
		for (var i=0; i<rows; i++){
			this.board[i] = min_cols+rand(max_cols + 1 - min_cols);
			$("#board")[0].appendChild(new_row_element(i,this.board[i]));
		}
	}
	GAME.equalize_board = function(){
		var xor = 0;
		for (i in this.board){
			xor = xor ^ this.board[i]
		}
		row = this.board.length;
		this.board[row] = xor;
		$("#board")[0].appendChild(new_row_element(row,this.board[row]));
	}
	GAME.new_game = function(){
		this.randomize_board(3,7,1,8);
		this.equalize_board();
		this.to_remove = null;
		this.begin_new_turn();
	}
	GAME.restart_game = function(){
		var b = $("#board")[0];
		var loss_count = getCookie("loss_count");
		if (loss_count > 0 && loss_count <= 13){
			$("#fact_" + loss_count)[0].style.display = 'none'
		}
		while (b.childNodes.length > 0){
			b.removeChild(b.childNodes[0]);
		}
		$("#new_game")[0].style.display = 'none';
		remove_message();
		this.new_game();
	}
	GAME.toggle_cells = function(row, col){
		var r = $("#board")[0].childNodes[row];
		for (i = col; i < r.childNodes.length; i++){
			var c = r.childNodes[i].childNodes[0];
			var filename = c.getAttribute('src');
			if (filename.charAt(DIR.length) == 'x'){
				filename = DIR + filename.slice(1+DIR.length);				
			}
			else{
				var str = "x";
				filename = DIR + str + filename.slice(DIR.length);
			}
			c.setAttribute('src',filename);
		}
	}
	
	GAME.remove_from_row = function(row, col){
		if (this.to_remove != null && this.to_remove.row == row && this.to_remove.col == col){
			this.end_turn();
		}
		else{
			if (this.to_remove != null){
				this.toggle_cells(this.to_remove.row,this.to_remove.col);
			}
			this.to_remove = {};
			this.to_remove['row'] = row;
			this.to_remove['col'] = col;
			
			this.toggle_cells(row,col);
		}
	}
	
	GAME.remove_cell = function(row, col){
		r = $("#board")[0].childNodes[row];
		for (i = r.childNodes.length - 1; i >= col; i--){
			r.removeChild(r.childNodes[i]);
			this.board[row]--;
		}
	}
	GAME.finish_computer_turn = function(coords){
		this.remove_cell(coords.row, coords.col);
		if (this.is_board_empty()){
				this.computer_win();
			}
		else{
			this.begin_new_turn();
		}
	}
	GAME.end_turn = function(){
		if (this.to_remove != null){
			this.remove_cell(this.to_remove.row, this.to_remove.col);
			this.to_remove = null;
			if (this.is_board_empty()){
				this.player_win();
			}
			else{			
				coords = this.computer_choose();
				this.toggle_cells(coords.row, coords.col);
				window.setTimeout(function(){GAME.finish_computer_turn(coords)},500);
			}
		}
	}
	
	GAME.is_board_empty = function(){
		for (i in this.board){
			if (this.board[i] > 0){
				return false;
			}
		}
		return true;
	}
	
	GAME.computer_choose = function(){
		var xor = 0;
		var coords = {};
		for (i in this.board){
			xor = xor ^ this.board[i]
		}
		if (xor == 0){
			var starting_row = rand(this.board.length);
			for (var i = 0; i < this.board.length; i++){
				var current_row = (starting_row + i) % this.board.length;
				if (this.board[current_row] > 0){
					coords.row = current_row;
					coords.col = rand(this.board[current_row]);
					break;
				}
			}
		}
		else{
			var highest_power_of_two = 1;
			var temp_xor = xor;
			while (temp_xor > 1){
				temp_xor >>= 1;
				highest_power_of_two <<= 1;
			}
			var i = 0;
			while ((this.board[i] & highest_power_of_two) == 0){
				i += 1;
			}
			coords.row = i;
			coords.col = (this.board[i] ^ xor);
		}		
		return coords;
	}
	
	GAME.begin_new_turn = function(){
		var coords = this.computer_choose();
	}
	
	GAME.player_win = function(){
		$("#new_game")[0].style.display = 'inline'
	}
	
	GAME.computer_win = function(){
		$("#new_game")[0].style.display = 'inline'
		var loss_count = getCookie("loss_count");
		if (loss_count == null){
			loss_count = 0;
		}
		if (loss_count < 13){
			loss_count++;
			display_message(DIR + 'nelson.jpg',"חה חה! הפסדת בפעם ה-" + loss_count + "!");
			setCookie("loss_count", loss_count, 365);
			$("#fact_" + loss_count)[0].style.display = 'inline'
		}
		else{
			$("#final")[0].style.display = 'inline'
		}
	}
	
	GAME.new_game();
}

if(window.attachEvent) {
    window.attachEvent('onload', init);
} else {
    if(window.onload) {
        var curronload = window.onload;
        var newonload = function() {
            curronload();
            init();
        };
        window.onload = newonload;
    } else {
        window.onload = init;
    }
}
//window.onload = init
