const hexagons = document.querySelectorAll('.hexagon');
const centerHexagon = document.querySelector('#center');
const wordInput = document.querySelector('#wordInput');
const seedInput = document.querySelector('#seedInput');
const wordList = document.querySelector('#wordList');
const infoMessage = document.querySelector('#infoMessage');
const submitButton = document.querySelector('#submit');
let dictionary;
let pangrams;
let acceptedWords;
let score;
let wordsFound;

class SeededRNG {
    constructor(seed = 1) {
      this.m = 0x80000000; // 2**31;
      this.a = 1103515245;
      this.c = 12345;
  
      this.state = seed;
    }
  
    nextInt() {
      this.state = (this.a * this.state + this.c) % this.m;
      return this.state;
    }
  
    nextFloat() {
      // returns in range [0,1]
      return this.nextInt() / (this.m - 1);
    }
  }

const MESSAGES = {
    "key_not_in_hexagons": "ניתן להשתמש רק באותיות שמופיעות במשושים",
    "missing_middle_word": "האות שבמשושה האמצעי חייבת להיות חלק מהמילה",
    "word_not_in_dict": "המילה לא מופיעה במילון שאיתו עובד המשחק",
    "word_added": "יפה מאוד! המילה התווספה לרשימה",
    "word_already_accepted": "כבר מצאת את המילה הזו",
    "pangram_added": "כל הכבוד! מצאת פנגרמה!"
}

function convertLetter(letter) {
    // Mapping of English to Hebrew letters and vice versa
    const letterMap = {
        'a': 'ש',
        'e': 'ק',
        'r': 'ר',
        't': 'א',
        'y': 'ט',
        'u': 'ו',
        'i': 'נ',
        'o': 'מ',
        'p': 'פ',
        '[': ']',
        ']': '[',
        's': 'ד',
        'd': 'ג',
        'f': 'כ',
        'g': 'ע',
        'h': 'י',
        'j': 'ח',
        'k': 'ל',
        'l': 'כ',
        ';': 'פ',
        '\'': ',',
        'z': 'ז',
        'x': 'ס',
        'c': 'ב',
        'v': 'ה',
        'b': 'נ',
        'n': 'מ',
        'm': 'צ',
        ',': 'ת',
        '.': 'צ',
        '/': '.',
        // Hebrew letters from their final forms
        'ך': 'כ',
        'ם': 'מ',
        'ן': 'נ',
        'ף': 'פ',
        'ץ': 'צ',
    };

    return letterMap[letter] || letter;
}

// logic for handling letters with final form
const finalForm = {
    'כ': 'ך',
    'מ': 'ם',
    'נ': 'ן',
    'פ': 'ף',
    'צ': 'ץ',
};

const regularForm = {
    'ך': 'כ',
    'ם': 'מ',
    'ן': 'נ',
    'ף': 'פ',
    'ץ': 'צ',
};

function convertToFinalForm(word) {
    let newWord = '';
    for (let i = 0; i < word.length; i++) {
        let letter = word[i];

        // If letter has a regular form, use that
        if (regularForm[letter]) {
            letter = regularForm[letter];
        }

        // If it is the last letter and has a final form, use that
        if (i === word.length - 1 && finalForm[letter]) {
            letter = finalForm[letter];
        }

        newWord += letter;
    }
    return newWord;
}

function updateScore(newScore) {
    score = newScore;
    document.getElementById('scoreCounter').innerText = "ניקוד: " + score;
}

function updateWordsFound(newWordsFound) {
    wordsFound = newWordsFound;
    document.getElementById('wordCounter').innerText = "מספר מילים שנמצאו: " + wordsFound;
}

function msg(m = ""){
    if (m === ""){
        infoMessage.style.visibility = "hidden";
    } 
    else {
        infoMessage.textContent = MESSAGES[m];
        infoMessage.style.visibility = "visible";
    }
}
function initGame(seed) {
    // Seeded random number generator
    let rng = new SeededRNG(seed);
 
    // Shuffle the pangrams array
    let randomIndex = Math.floor(rng.nextFloat() * pangrams.length);
    let randomElement = pangrams[randomIndex];
    let uniqueLetters = new Set(randomElement);
    let letters = Array.from(uniqueLetters).join('');    
    // Shuffle the letters array
    for (let i = letters.length - 1; i > 0; i--) {
        const j = Math.floor(rng.nextFloat() * (i + 1));
        [letters[i], letters[j]] = [letters[j], letters[i]];
    }
    // Set the letters to the hexagons
    let hexagons = document.getElementsByClassName("hexagon");
    for(let i=0; i<hexagons.length; i++) {
        letter = letters[i];
        if (regularForm[letter]) {
            letter = regularForm[letter];
        }
        hexagons[i].innerText = letter;
    }
    acceptedWords = [];
    seedInput.value = seed;
    wordList.innerHTML = "";
    updateScore(0);
    updateWordsFound(0);
}

fetch('dictionary.json')
  .then(response => response.json())
  .then(data => dictionary = data);

fetch('pangrams.json')
  .then(response => response.json())
  .then(data => {
    pangrams = data;
    // Get today's date and generate a seed
    let today = new Date();
    seed = today.getFullYear() * 10000 + (today.getMonth()+1) * 100 + today.getDate();
    console.log(seed);
    // Initialize the game with the seed
    initGame(seed);
});


// Add click event listeners to the hexagons
hexagons.forEach(hexagon => {
    hexagon.addEventListener('click', event => {
        // Add the clicked hexagon's letter to the word input
        wordInput.value = convertToFinalForm(wordInput.value + event.target.textContent);
    });
});

document.addEventListener('keydown', event => {
    if (document.activeElement === seedInput){
        return;
    }
    const hexagonLetters = [...hexagons].map(h => h.textContent);
    const key = convertLetter(event.key);
    // If the key is a letter in the hexagons, add it to the word input
    if (hexagonLetters.includes(key)) {
      wordInput.value = convertToFinalForm(wordInput.value + key);
      event.preventDefault(); // prevent the default behavior
      msg("");
    } 
    else if (key === 'Backspace') {
      wordInput.value = convertToFinalForm(wordInput.value.slice(0, -1));
      event.preventDefault(); // prevent the default behavior
      msg("");
    }
    else if (key === 'Enter') {
        checkWord();
    }
    else {
        msg('key_not_in_hexagons');
    }
  });

document.getElementById("clear").addEventListener("click", function() {
    wordInput.value = '';
});

submitButton.addEventListener('click', checkWord);

function checkWord() {
  let word = wordInput.value;
  if (acceptedWords.includes(word)) {
    msg('word_already_accepted');
    return;
  }
  let letters = Array.from(new Set(word)); // Ensure no repeated letters
  
  // Check that each letter is in the hexagons
  for (let letter of letters) {
    if (regularForm[letter]) {
        letter = regularForm[letter];
    }
    if (![...hexagons].map(h => h.textContent).includes(letter)) {
      msg('key_not_in_hexagons');
      return;
    }
  }

  // Check that the center letter is in the word
  if (!word.includes(centerHexagon.textContent)) {
    msg('missing_middle_word');
    return;
  }

  // Check that the word is in the dictionary
  if (!dictionary.includes(word)) {
    msg('word_not_in_dict');
    return;
  }

  // If the word passes all checks, add it to the list and clear the input
  let listItem = document.createElement('li');
  listItem.textContent = word;

  wordList.appendChild(listItem);
  // scroll to bottom of list
  wordList.scrollTop = wordList.scrollHeight;

  acceptedWords.push(word);
  wordInput.value = '';
  updateWordsFound(wordsFound + 1);
   // Get unique letters from hexagons
   const gameLetters = Array.from(new Set([...hexagons].map(h => h.textContent)));

   // Ensure no repeated letters in the word
   let wordLetters = Array.from(new Set(word.split(''))).map(letter => regularForm[letter] || letter);
 
   // Check if the word contains all game letters
  const containsAllLetters = gameLetters.every(letter => wordLetters.includes(letter));
 
  if (containsAllLetters) {
    updateScore(5 + score + word.length - 1);
    msg('pangram_added');
  } else {
    updateScore(score + word.length - 1);
    msg('word_added');
  }
}

document.querySelector('#newGame').addEventListener('click', () => {
    submitButton.focus();
    let seed = seedInput.value;
    initGame(seed);
});