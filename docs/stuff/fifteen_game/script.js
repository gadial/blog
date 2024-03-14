const puzzleContainer = document.getElementById('puzzle-container');
const moveCounter = document.getElementById('move-counter');
let moves = 0;

function createPuzzle() {
//    const pieces = [...Array(15).keys()].map(n => n + 1).concat([null]);
//    pieces.sort(() => Math.random() - 0.5);
    const pieces = [15, 2, 1, 12, 4, 9, 10, 7, 8, 5, 6, 11, 3, 14, 13, null];
    pieces.forEach(value => {
        const piece = document.createElement('div');
        piece.className = 'puzzle-piece';
        piece.textContent = value;        
        piece.addEventListener('click', () => movePiece(piece));
        puzzleContainer.appendChild(piece);
    });
}

function movePiece(piece) {
    const index = [...puzzleContainer.children].indexOf(piece);
    const emptyIndex = [...puzzleContainer.children].findIndex(child => !child.textContent);
    const [x, y] = [index % 4, Math.floor(index / 4)];
    const [emptyX, emptyY] = [emptyIndex % 4, Math.floor(emptyIndex / 4)];
    if (Math.abs(x - emptyX) + Math.abs(y - emptyY) === 1) {
        puzzleContainer.children[emptyIndex].textContent = piece.textContent;
        piece.textContent = '';
        moves++;
        moveCounter.textContent = `Moves: ${moves}`;
    }
    updateSums();
}

function updateSums() {
    const grid = [...puzzleContainer.children].map(piece => parseInt(piece.textContent) || 0);
    const rowSums = [0, 0, 0, 0];
    const colSums = [0, 0, 0, 0];
    let diagSum1 = 0;
    let diagSum2 = 0;

    for (let i = 0; i < 4; i++) {
        for (let j = 0; j < 4; j++) {
            const value = grid[i * 4 + j];
            rowSums[i] += value;
            colSums[j] += value;
            if (i === j) diagSum1 += value;
            if (i + j === 3) diagSum2 += value;
        }
    }

    document.getElementById('row-sums').textContent = `Row Sums: ${rowSums.join(', ')} ${rowSums.every(sum => sum === 30) ? '✅' : '❌'}`;
    document.getElementById('col-sums').textContent = `Column Sums: ${colSums.join(', ')} ${colSums.every(sum => sum === 30) ? '✅' : '❌'}`;
    document.getElementById('diag-sums').textContent = `Diagonal Sums: ${diagSum1}, ${diagSum2} ${(diagSum1 === 30 && diagSum2 === 30) ? '✅' : '❌'}`;
}

createPuzzle();
updateSums();