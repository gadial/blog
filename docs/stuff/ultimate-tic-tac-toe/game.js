(() => {
  "use strict";

  const LINES = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
  ];

  const boardElement = document.querySelector("#board");
  const statusLabel = document.querySelector("#status-label");
  const statusHint = document.querySelector("#status-hint");
  const turnMark = document.querySelector("#turn-mark");
  const moveCount = document.querySelector("#move-count");
  const undoButton = document.querySelector("#undo");
  const redoButton = document.querySelector("#redo");
  const newGameButton = document.querySelector("#new-game");
  const rulesButton = document.querySelector("#rules-button");
  const rules = document.querySelector("#rules");

  let moves = [];
  let cursor = 0;

  function winner(cells) {
    for (const [a, b, c] of LINES) {
      if (cells[a] && cells[a] === cells[b] && cells[a] === cells[c]) return cells[a];
    }
    return null;
  }

  function deriveState() {
    const boards = Array.from({ length: 9 }, () => Array(9).fill(null));
    for (const move of moves.slice(0, cursor)) boards[move.board][move.cell] = move.player;

    const results = boards.map((cells) => winner(cells) || (cells.every(Boolean) ? "draw" : null));
    const meta = results.map((result) => result === "X" || result === "O" ? result : null);
    const gameWinner = winner(meta);
    const gameOver = Boolean(gameWinner) || results.every(Boolean);
    const lastMove = cursor ? moves[cursor - 1] : null;
    const target = lastMove && !results[lastMove.cell] ? lastMove.cell : null;
    const player = cursor % 2 === 0 ? "X" : "O";
    return { boards, results, gameWinner, gameOver, target, player };
  }

  function isLegal(state, board, cell) {
    return !state.gameOver && !state.results[board] && !state.boards[board][cell] &&
      (state.target === null || state.target === board);
  }

  function play(board, cell) {
    const state = deriveState();
    if (!isLegal(state, board, cell)) return;
    moves = moves.slice(0, cursor);
    moves.push({ board, cell, player: state.player });
    cursor += 1;
    render();
  }

  function render() {
    const state = deriveState();
    boardElement.replaceChildren();

    state.boards.forEach((cells, boardIndex) => {
      const miniBoard = document.createElement("section");
      const openForPlay = !state.gameOver && !state.results[boardIndex] &&
        (state.target === null || state.target === boardIndex);
      miniBoard.className = `mini-board${openForPlay ? " active" : ""}${state.results[boardIndex] ? " closed" : ""}`;
      miniBoard.setAttribute("role", "rowgroup");
      miniBoard.setAttribute("aria-label", `Small board ${boardIndex + 1}${openForPlay ? ", available" : ""}`);

      cells.forEach((mark, cellIndex) => {
        const cell = document.createElement("button");
        const legal = isLegal(state, boardIndex, cellIndex);
        cell.type = "button";
        cell.className = `cell${mark ? ` ${mark.toLowerCase()}` : ""}${legal ? " legal" : ""}`;
        cell.textContent = mark || "";
        cell.disabled = !legal;
        cell.setAttribute("role", "gridcell");
        cell.setAttribute("aria-label", `Board ${boardIndex + 1}, square ${cellIndex + 1}${mark ? `, ${mark}` : legal ? ", available" : ", unavailable"}`);
        cell.addEventListener("click", () => play(boardIndex, cellIndex));
        miniBoard.append(cell);
      });

      if (state.results[boardIndex]) {
        const result = document.createElement("div");
        result.className = `mini-result ${state.results[boardIndex].toLowerCase()}`;
        result.textContent = state.results[boardIndex] === "draw" ? "—" : state.results[boardIndex];
        result.setAttribute("aria-hidden", "true");
        miniBoard.append(result);
      }
      boardElement.append(miniBoard);
    });

    moveCount.textContent = cursor;
    undoButton.disabled = cursor === 0;
    redoButton.disabled = cursor === moves.length;

    if (state.gameWinner) {
      statusLabel.textContent = `${state.gameWinner} wins the game`;
      statusHint.textContent = "Undo a move or start a new game";
      turnMark.textContent = state.gameWinner;
      turnMark.className = `turn-mark ${state.gameWinner.toLowerCase()}`;
    } else if (state.gameOver) {
      statusLabel.textContent = "The game is a draw";
      statusHint.textContent = "Undo a move or start a new game";
      turnMark.textContent = "—";
      turnMark.className = "turn-mark";
    } else {
      statusLabel.textContent = `${state.player} to play`;
      statusHint.textContent = state.target === null
        ? "Choose any glowing square"
        : `Play in glowing board ${state.target + 1}`;
      turnMark.textContent = state.player;
      turnMark.className = `turn-mark ${state.player.toLowerCase()}`;
    }
  }

  undoButton.addEventListener("click", () => { if (cursor > 0) { cursor -= 1; render(); } });
  redoButton.addEventListener("click", () => { if (cursor < moves.length) { cursor += 1; render(); } });
  newGameButton.addEventListener("click", () => { moves = []; cursor = 0; render(); });
  rulesButton.addEventListener("click", () => {
    const showing = rules.hidden;
    rules.hidden = !showing;
    rulesButton.setAttribute("aria-expanded", String(showing));
  });
  document.addEventListener("keydown", (event) => {
    const modifier = event.ctrlKey || event.metaKey;
    const key = event.key.toLowerCase();
    const undoShortcut = modifier && key === "z" && !event.shiftKey;
    const redoShortcut = modifier && (key === "y" || (key === "z" && event.shiftKey));
    if (!undoShortcut && !redoShortcut) return;
    event.preventDefault();
    if (redoShortcut) redoButton.click(); else undoButton.click();
  });

  render();
})();
