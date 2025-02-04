var BIBLE_MAIN = {}
var PURE_TEXT_ID = "#pure_text"
var ORIGINAL_TEXT_ID = "#original_text"
var LISTS_ID = "#lists"
var WORD_LIST_ID = "#word_list"
var ELS_LIST_ID = "#els_list"
var MSG_BOX_ID = "#msgbox"

function loadTextFromFile(filename){
	var result;
	$.get(filename, function(data){
		result = data;
	},'text')
	return result;	
}

var init = function() {
	BIBLE_MAIN.sessions = [];
	
	BIBLE_MAIN.print = function(msg){
				$(MSG_BOX_ID)[0].innerHTML = msg;
	}
	
	BIBLE_MAIN.findWord = function(words, min_jump, max_jump){
		this.active_session.postMessage({'type': 'find_words', 'words': words, 'min_jump': min_jump, 'max_jump':max_jump});
		// words = words.replace(/\s+/g," ");
		// var words_array = words.split(" ");
		// for (var i=0; i<words_array.length; i++){
			// word = words_array[i];
			// //this.active_session.findAndColorWord(word);
			// this.els_find_worker.postMessage({'type': 'findEls', 'text': this.active_session.pure_text, 'str':word});
		// }
	}
	BIBLE_MAIN.addWordToList = function(word, color, length){
		var o = new Option(word + " (" + length + ")", word);
		o.style.backgroundColor = color;
		o.onclick = function(){
			BIBLE_MAIN.fillElsListFor(word);
		}
		$(WORD_LIST_ID)[0].add(o);
	}
	
	BIBLE_MAIN.fillElsListFor = function(word){
		this.active_session.postMessage({'type': 'fill_els_list_for', 'word': word});
	}
	
	BIBLE_MAIN.fillElsList = function(els_array){
		var list = document.createElement("select");
		// var els_array = this.els_list[word];
		
		list.id = ELS_LIST_ID.replace("#","");
		list.size = 6;
		
		for (i=0; i<els_array.length; i++){
			var els = els_array[i];
			var option = new Option("(" + els.index + ", " + els.jump + ")", i);
			option.jump_to_location = els.index;
			option.jump_size = Math.abs(els.jump);
			option.onclick = function(){
				BIBLE_MAIN.jumpToWord(this.jump_to_location, this.jump_size);
			}
			list.add(option);			
		}
		$(LISTS_ID)[0].removeChild($(ELS_LIST_ID)[0]);
		$(LISTS_ID)[0].appendChild(list);
	}
	BIBLE_MAIN.jumpToWord = function (word_location, word_jump_size){
		message = {'type': 'goto_word', 'word_location': word_location};
		if (word_jump_size > 5){ //otherwise it looks bad
			message.word_jump_size = word_jump_size;
			// BIBLE_MAIN.changePureTextJumpSize(word_jump_size);
		}
		this.active_session.postMessage(message);
	}
	
	BIBLE_MAIN.start_first_session = function(text){
		var first_session = newSession(text);
		//var first_session = newSession(heb_lorem_ipsum_text);
		//var first_session = newSession(genesis_text);
		//var first_session = newSession(torah_text);
		this.active_session = first_session;
		this.sessions.push(this.active_session);
		//this.active_session.update();
	}
	
	BIBLE_MAIN.start_new_session = function(text_filename){
		var session = new Worker('session.js');
		session.onmessage = function(event){
			switch (event.data.type){
				case 'message':
					BIBLE_MAIN.print(event.data.message);	
					break;
				case 'log':
					console.log("Session " + text_filename + " says: " + event.data.message);
					break;
				case 'update_pure_text':
					console.log("Session " + text_filename + " asks for pure text update");
					$(PURE_TEXT_ID)[0].innerHTML = event.data.pure_text;
					// BIBLE_MAIN.slowlyUpdateText($(PURE_TEXT_ID)[0], event.data.pure_text);
					console.log("update done");
					break;
				case 'update_original_text':
					console.log("Session " + text_filename + " asks for original text update");
					$(ORIGINAL_TEXT_ID)[0].innerHTML = event.data.original_text;
					// BIBLE_MAIN.slowlyUpdateText($(ORIGINAL_TEXT_ID)[0], event.data.original_text);
					// $(ORIGINAL_TEXT_ID)[0].appendChild(document.createTextNode(event.data.original_text));

					console.log("update done");
					break;	
				case 'add_word_to_list':
					BIBLE_MAIN.addWordToList(event.data.word, event.data.color, event.data.length);
					break;
				case 'fill_els_list':
					BIBLE_MAIN.fillElsList(event.data.els_array);
					break;	
				case 'goto_word':
					window.location = "#original_text" + event.data.word_location;
					window.location = "#pure_text" + event.data.word_location;
					window.location = "#";		
					break;
			}
		}
		this.active_session = session;
		this.sessions.push(session);
		
		$.get(text_filename, function(data){
			text_node = $(data).find("text")[0];
			text_node.normalize(); 
			text = text_node.childNodes[0].nodeValue;
			session.postMessage({'type': 'init', 'text_filename': text});
		},'xml')
	}
	
	BIBLE_MAIN.changePureTextJumpSize = function(new_jump_size){
		this.active_session.postMessage({'type': 'change_jump_size', 'new_jump_size': new_jump_size});	
	}
	BIBLE_MAIN.slowlyUpdateText = function(textbox, text_chunks){
		textbox.innerHTML = "";
		for (i = 0; i < text_chunks.length; i++){
			setTimeout(function(x){
				return function(){
					textbox.innerHTML += text_chunks[x];
				}
			}(i), 0);
		}
	}
	
	BIBLE_MAIN.els_find_worker = new Worker('els_find_worker.js');  
	BIBLE_MAIN.els_find_worker.onmessage = function(event) {  
  		if (event.data.type == 'findElsResult'){
  			BIBLE_MAIN.active_session.addEls(event.data.word, event.data.result);
  		}
	};
	//var alice_text = loadTextFromFile("alice.txt");
	//var alice_text = $("#alice_text")[0].innerHTML;
//	$.get("alice.txt", function(data){
//		BIBLE_MAIN.texts.alice = data; 
//		BIBLE_MAIN.start_first_session(BIBLE_MAIN.texts.alice);	
//		},'text');
	 
	//BIBLE_MAIN.active_session.findAndColorWord('where');
	//BIBLE_MAIN.active_session.findAndColorWord('when');
	//BIBLE_MAIN.start_first_session("maavar.xml");
	//BIBLE_MAIN.start_first_session("genesis.xml");
// 	BIBLE_MAIN.start_new_session("genesis.xml");
	BIBLE_MAIN.start_new_session("torah.xml");
// 	BIBLE_MAIN.start_new_session("wikitext.xml");
}

window.onload = init
