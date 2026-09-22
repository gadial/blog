(() => {
  const copy = {
    he: { eyebrow:'אותיות נפגשות באמצע', title:'פלינדרומים<br>וריבועי קסם', intro:'שני כלים קטנים למשחק בסימטריה של מילים.', sentenceTitle:'משפט פלינדרומי', sentenceHelp:'כתבו התחלה, ואנחנו נשלים אותה בהשתקפות. רווחים אינם נספרים.', sentenceLabel:'ההתחלה שלכם', sentencePlaceholder:'למשל: אב גד', resultLabel:'הפלינדרום', resultHint:'לחצו בין אותיות כדי להוסיף או להסיר רווח', squareTitle:'ריבוע קסם', squareHelp:'מלאו אות בכל משבצת. כל שינוי משתקף במשבצת התואמת, כך שהשורות והעמודות נקראות באופן זהה.', sizeLabel:'גודל הריבוע', clear:'ניקוי', squareNote:'השורות נקראות מלמעלה למטה; העמודות מימין לשמאל.', switchLanguage:'Switch to English', switchLabel:'English', resultAria:'הפלינדרום המלא', squareAria:n => `ריבוע קסם ${n} על ${n}`, smaller:'הקטנת הריבוע', larger:'הגדלת הריבוע', cell:(r,c)=>`שורה ${r}, עמודה ${c}` },
    en: { eyebrow:'Letters meet in the middle', title:'Palindromes<br>& word squares', intro:'Two small tools for playing with the symmetry of words.', sentenceTitle:'Palindrome builder', sentenceHelp:'Write a beginning and we’ll complete its reflection. Spaces do not count.', sentenceLabel:'Your beginning', sentencePlaceholder:'For example: never odd', resultLabel:'The palindrome', resultHint:'Click between letters to add or remove a space', squareTitle:'Word square', squareHelp:'Enter one letter in each cell. Every change is reflected in its matching cell, so rows and columns read alike.', sizeLabel:'Square size', clear:'Clear', squareNote:'Rows read from top to bottom; columns read from left to right.', switchLanguage:'החלפה לעברית', switchLabel:'עברית', resultAria:'The complete palindrome', squareAria:n => `${n} by ${n} word square`, smaller:'Make square smaller', larger:'Make square larger', cell:(r,c)=>`Row ${r}, column ${c}` }
  };

  let lang = 'he';
  let size = 5;
  let values = Array(size * size).fill('');
  let customSpaces = new Set();
  const input = document.querySelector('#sentence-input');
  const result = document.querySelector('#palindrome-result');
  const square = document.querySelector('#magic-square');

  function lettersOnly(text) { return Array.from(text).filter(char => !/\s/u.test(char)); }

  function renderPalindrome(resetSpaces = false) {
    const typed = input.value;
    const first = lettersOnly(typed);
    const all = first.concat([...first].reverse());
    if (resetSpaces) {
      customSpaces = new Set();
      let letterIndex = 0;
      for (const char of Array.from(typed)) {
        if (/\s/u.test(char) && letterIndex > 0 && letterIndex < first.length) customSpaces.add(letterIndex - 1);
        else if (!/\s/u.test(char)) letterIndex++;
      }
    }
    [...customSpaces].forEach(i => { if (i >= all.length - 1) customSpaces.delete(i); });
    result.replaceChildren();
    all.forEach((char, i) => {
      const letter = document.createElement('span');
      letter.className = 'letter';
      letter.textContent = char;
      result.append(letter);
      if (i < all.length - 1) {
        const gap = document.createElement('button');
        gap.type = 'button';
        gap.className = `gap${customSpaces.has(i) ? ' has-space' : ''}`;
        gap.setAttribute('aria-label', customSpaces.has(i) ? 'Remove space' : 'Add space');
        gap.addEventListener('click', () => { customSpaces.has(i) ? customSpaces.delete(i) : customSpaces.add(i); renderPalindrome(); });
        result.append(gap);
      }
    });
  }

  function cleanLetter(value) {
    return Array.from(value.normalize('NFC')).filter(c => !/\s/u.test(c)).slice(-1)[0] || '';
  }

  function equivalentCells(row, col) {
    const last = size - 1;
    return new Set([
      row * size + col,                         // The edited cell.
      col * size + row,                         // Rows equal columns.
      (last - row) * size + (last - col),       // The whole text is palindromic.
      (last - col) * size + (last - row)        // Both constraints together.
    ]);
  }

  function renderSquare() {
    square.style.setProperty('--size', size);
    square.setAttribute('aria-label', copy[lang].squareAria(size));
    document.querySelector('#square-size').textContent = `${size} × ${size}`;
    square.replaceChildren();
    for (let row = 0; row < size; row++) {
      for (let col = 0; col < size; col++) {
        const cell = document.createElement('input');
        const index = row * size + col;
        cell.className = 'cell'; cell.value = values[index] || '';
        cell.maxLength = 2; cell.autocomplete = 'off'; cell.spellcheck = false;
        cell.setAttribute('role', 'gridcell');
        cell.setAttribute('aria-label', copy[lang].cell(row + 1, col + 1));
        cell.addEventListener('input', () => {
          const letter = cleanLetter(cell.value);
          cell.value = letter;
          equivalentCells(row, col).forEach(equivalentIndex => {
            values[equivalentIndex] = letter;
            const equivalent = square.children[equivalentIndex];
            if (!equivalent || equivalent === cell) return;
            equivalent.value = letter;
            equivalent.classList.remove('mirror-flash');
            void equivalent.offsetWidth;
            equivalent.classList.add('mirror-flash');
          });
        });
        square.append(cell);
      }
    }
  }

  function resizeSquare(nextSize) {
    if (nextSize < 2 || nextSize > 9 || nextSize === size) return;
    size = nextSize;
    values = Array(size * size).fill('');
    renderSquare();
  }

  function applyLanguage() {
    const t = copy[lang];
    document.documentElement.lang = lang; document.documentElement.dir = lang === 'he' ? 'rtl' : 'ltr';
    document.title = lang === 'he' ? 'פלינדרומים וריבועי קסם' : 'Palindromes & word squares';
    document.querySelectorAll('[data-i18n]').forEach(el => el.innerHTML = t[el.dataset.i18n]);
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => el.placeholder = t[el.dataset.i18nPlaceholder]);
    const toggle = document.querySelector('#language-toggle'); toggle.textContent = t.switchLabel; toggle.setAttribute('aria-label', t.switchLanguage);
    result.setAttribute('aria-label', t.resultAria);
    document.querySelector('#size-down').setAttribute('aria-label', t.smaller);
    document.querySelector('#size-up').setAttribute('aria-label', t.larger);
    renderSquare();
  }

  input.addEventListener('input', () => renderPalindrome(true));
  document.querySelector('#language-toggle').addEventListener('click', () => { lang = lang === 'he' ? 'en' : 'he'; applyLanguage(); });
  document.querySelector('#size-down').addEventListener('click', () => resizeSquare(size - 1));
  document.querySelector('#size-up').addEventListener('click', () => resizeSquare(size + 1));
  document.querySelector('#clear-square').addEventListener('click', () => { values.fill(''); renderSquare(); square.querySelector('.cell').focus(); });
  renderPalindrome(); applyLanguage();
})();
