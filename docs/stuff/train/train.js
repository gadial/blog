// Train & Wagon Arithmetic Game
// Core JavaScript + HTML implementation

const BOARD_LENGTH = 51;
const TOWNS = [10, 20, 30, 40, 50];
const OPERATORS = ['+', '-', '*', '/'];

let gameState = {
    players: [
        { name: 'Locomotive', pos: 0 },
        { name: 'Wagon', pos: 0 },
    ],
    currentPlayer: 0,
    numbers: [],
    expression: [],
    usedOps: new Set(),
    result: null
};

function generateNumbers() {
    gameState.numbers = [];
    while (gameState.numbers.length < 4) {
        let n = Math.floor(Math.random() * 9) + 1;
        gameState.numbers.push(n);
    }
}

function resetExpression() {
    gameState.expression = [];
    gameState.usedOps = new Set();
    gameState.result = null;
}

function updateBoard() {
    const board = document.getElementById('board');
    board.innerHTML = '';
    for (let i = 0; i < BOARD_LENGTH; i++) {
        const cell = document.createElement('div');
        cell.className = 'cell';
        if (TOWNS.includes(i)) cell.classList.add('town');
        gameState.players.forEach((p, idx) => {
            if (p.pos === i) {
                const marker = document.createElement('span');
                marker.textContent = idx === 0 ? '🚂' : '🚗';
                cell.appendChild(marker);
            }
        });
        cell.textContent += i;
        board.appendChild(cell);
    }
    document.getElementById('player-info').textContent = `${gameState.players[gameState.currentPlayer].name}'s turn`;
}

function renderOptions() {
    const numbers = document.getElementById('numbers');
    numbers.innerHTML = '';
    gameState.numbers.forEach((n, idx) => {
        const btn = document.createElement('button');
        btn.textContent = n;
        btn.onclick = () => selectNumber(n);
        numbers.appendChild(btn);
    });

    const ops = document.getElementById('operators');
    ops.innerHTML = '';
    OPERATORS.forEach(op => {
        const btn = document.createElement('button');
        btn.textContent = op;
        btn.disabled = gameState.usedOps.has(op);
        btn.onclick = () => selectOperator(op);
        ops.appendChild(btn);
    });

    document.getElementById('expression').textContent = gameState.expression.join(' ');
    document.getElementById('result').textContent = gameState.result !== null ? `= ${gameState.result}` : '';
}

function selectNumber(n) {
    gameState.expression.push(n);
    evaluateExpression();
    renderOptions();
}

function selectOperator(op) {
    if (!gameState.usedOps.has(op)) {
        gameState.expression.push(op);
        gameState.usedOps.add(op);
        renderOptions();
    }
}

function evaluateExpression() {
    try {
        const expr = gameState.expression.join(' ');
        const val = Function(`return ${expr}`)();
        if (!isNaN(val) && isFinite(val)) {
            gameState.result = Math.floor(val);
        }
    } catch {
        gameState.result = null;
    }
}

function commitMove() {
    if (gameState.result === null) return alert('Invalid expression');
    let p = gameState.players[gameState.currentPlayer];
    p.pos += gameState.result;
    while (TOWNS.includes(p.pos) && p.pos < 50) {
        const idx = TOWNS.indexOf(p.pos);
        p.pos = TOWNS[idx + 1];
    }
    if (p.pos >= 50) {
        alert(`${p.name} wins!`);
        startGame();
        return;
    }
    gameState.currentPlayer = 1 - gameState.currentPlayer;
    generateNumbers();
    resetExpression();
    updateBoard();
    renderOptions();
}

function startGame() {
    gameState.players = [
        { name: 'Locomotive', pos: 0 },
        { name: 'Wagon', pos: 0 },
    ];
    gameState.currentPlayer = 0;
    generateNumbers();
    resetExpression();
    updateBoard();
    renderOptions();
}

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('ok-btn').onclick = commitMove;
    startGame();
});
