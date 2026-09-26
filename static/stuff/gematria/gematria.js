"use strict";

const letterValues = Object.freeze({
  א: 1, ב: 2, ג: 3, ד: 4, ה: 5, ו: 6, ז: 7, ח: 8, ט: 9,
  י: 10, כ: 20, ך: 20, ל: 30, מ: 40, ם: 40, נ: 50, ן: 50,
  ס: 60, ע: 70, פ: 80, ף: 80, צ: 90, ץ: 90, ק: 100,
  ר: 200, ש: 300, ת: 400
});

const primaryInput = document.querySelector("#primary_word");
const secondaryInput = document.querySelector("#secondary_word");
const primaryValue = document.querySelector("#primary_value");
const secondaryValue = document.querySelector("#secondary_value");
const differenceValue = document.querySelector("#gematric_difference");
const wordList = document.querySelector("#word_list");
const matchesStatus = document.querySelector("#matches_status");
const matchCount = document.querySelector("#match_count");

function computeValue(text) {
  return Array.from(text).reduce((sum, letter) => sum + (letterValues[letter] || 0), 0);
}

// The original dictionary was saved as UTF-8 text interpreted as Latin-1.
const utf8Decoder = new TextDecoder("utf-8");
const windows1252Bytes = new Map([
  ["€", 0x80], ["‚", 0x82], ["ƒ", 0x83], ["„", 0x84], ["…", 0x85],
  ["†", 0x86], ["‡", 0x87], ["ˆ", 0x88], ["‰", 0x89], ["Š", 0x8a],
  ["‹", 0x8b], ["Œ", 0x8c], ["Ž", 0x8e], ["‘", 0x91], ["’", 0x92],
  ["“", 0x93], ["”", 0x94], ["•", 0x95], ["–", 0x96], ["—", 0x97],
  ["˜", 0x98], ["™", 0x99], ["š", 0x9a], ["›", 0x9b], ["œ", 0x9c],
  ["ž", 0x9e], ["Ÿ", 0x9f]
]);
function repairDictionaryWord(word) {
  if (!word.includes("×")) return word;
  const bytes = Uint8Array.from(word, character =>
    windows1252Bytes.get(character) ?? (character.charCodeAt(0) & 0xff)
  );
  return utf8Decoder.decode(bytes);
}

function renderMatches(value, hasInput) {
  wordList.replaceChildren();
  matchCount.hidden = true;

  if (!hasInput) {
    matchesStatus.textContent = "הקלידו ביטוי כדי לראות הצעות.";
    return;
  }

  const words = typeof dic === "object" ? dic[value] : undefined;
  if (!words?.length) {
    matchesStatus.textContent = `לא נמצאו מילים במילון שערכן ${value}.`;
    return;
  }

  const fragment = document.createDocumentFragment();
  for (const word of words) {
    const item = document.createElement("li");
    item.textContent = repairDictionaryWord(word);
    fragment.appendChild(item);
  }
  wordList.appendChild(fragment);
  matchesStatus.textContent = `הצעות שערכן ${value}`;
  matchCount.textContent = words.length.toLocaleString("he-IL");
  matchCount.hidden = false;
}

function updateCalculator() {
  const first = computeValue(primaryInput.value);
  const second = computeValue(secondaryInput.value);
  const difference = Math.abs(first - second);

  primaryValue.value = first;
  secondaryValue.value = second;
  differenceValue.textContent = difference;
  renderMatches(difference, Boolean(primaryInput.value.trim() || secondaryInput.value.trim()));
}

primaryInput.addEventListener("input", updateCalculator);
secondaryInput.addEventListener("input", updateCalculator);
updateCalculator();
