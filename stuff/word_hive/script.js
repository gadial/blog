const hexagons = document.querySelectorAll('.hexagon');
const centerHexagon = document.querySelector('#center');
const wordInput = document.querySelector('#wordInput');
const wordList = document.querySelector('#wordList');
const infoMessage = document.querySelector('#infoMessage');
let dictionary;
let pangrams;
let acceptedWords;

const MESSAGES = {
    "key_not_in_hexagons": "ניתן להשתמש רק באותיות שמופיעות במשושים",
    "missing_middle_word": "האות שבמשושה האמצעי חייבת להיות חלק מהמילה",
    "word_not_in_dict": "המילה לא מופיעה במילון שאיתו עובד המשחק",
    "word_added": "יפה מאוד! המילה התווספה לרשימה",
    "word_already_accepted": "כבר מצאת את המילה הזו"
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
    function seedRandom(seed) {
        const a = 16807; // multiplier
        const m = 2147483647; // 2**31 - 1
        seed = seed * a % m;
        return seed / m;
    }
 
    // Shuffle the pangrams array
    let randomIndex = Math.floor(seedRandom(seed) * pangrams.length);
    let randomElement = pangrams[randomIndex];
    let uniqueLetters = new Set(randomElement);
    let letters = Array.from(uniqueLetters).join('');    
    // Shuffle the letters array
    for (let i = letters.length - 1; i > 0; i--) {
        const j = Math.floor(seedRandom(seed) * (i + 1));
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
}

fetch('dictionary.json')
  .then(response => response.json())
  .then(data => dictionary = data);

// Get today's date and generate a seed
let today = new Date();
seed = today.getFullYear() * 10000 + (today.getMonth()+1) * 100 + today.getDate();
// Initialize the game with the seed
fetch('pangrams.json')
  .then(response => response.json())
  .then(data => {
    pangrams = data;
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

document.querySelector('#submit').addEventListener('click', checkWord);

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
  msg('word_added');
}
