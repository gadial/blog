class TrainGame {
    constructor() {
        this.players = [
            { position: 0, isComputer: false },
            { position: 0, isComputer: false } // Disabled computer player
        ];
        this.currentPlayer = 0;
        this.numbers = [];
        this.expression = [];
        this.usedNumbers = new Set();
        this.usedOperations = new Set();
        this.towns = [10, 20, 30, 40, 50];
        this.gameOver = false;

        // Wait for DOM to be fully loaded
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.initialize());
        } else {
            this.initialize();
        }
    }

    initialize() {
        this.initializeBoard();
        this.initializeEventListeners();
        this.startNewTurn();
    }

    initializeBoard() {
        const boardTrack = document.getElementById('board-track');
        if (!boardTrack) {
            console.error('Board track element not found');
            return;
        }
        
        boardTrack.innerHTML = ''; // Clear any existing content

        // Create 5x10 grid of squares
        for (let row = 0; row < 5; row++) {
            for (let col = 0; col < 10; col++) {
                const position = row * 10 + col + 1;
                const square = document.createElement('div');
                square.className = 'board-square';
                if (this.towns.includes(position)) {
                    square.classList.add('town');
                }
                square.textContent = position;
                boardTrack.appendChild(square);
            }
        }

        // Remove any existing tokens
        document.querySelectorAll('.player-token').forEach(token => token.remove());

        // Add player tokens
        this.players.forEach((player, index) => {
            const token = document.createElement('div');
            token.className = 'player-token';
            token.id = `token-${index + 1}`;
            token.textContent = '🚂'; // Add train emoji
            boardTrack.appendChild(token);
        });

        // Position tokens after a short delay to ensure DOM is updated
        setTimeout(() => {
            this.players.forEach((_, index) => this.updateTokenPosition(index));
        }, 0);
    }

    initializeEventListeners() {
        // Number buttons
        document.getElementById('numbers').addEventListener('click', (e) => {
            if (e.target.classList.contains('number') && !e.target.classList.contains('used')) {
                this.selectNumber(parseInt(e.target.textContent));
            }
        });

        // Operation buttons
        document.querySelectorAll('.op-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                if (!btn.disabled) {
                    this.selectOperation(btn.dataset.op);
                }
            });
        });

        // Clear button
        document.getElementById('clear-btn').addEventListener('click', () => {
            this.clearExpression();
        });

        // Submit button
        document.getElementById('submit-btn').addEventListener('click', () => {
            this.submitMove();
        });
    }

    startNewTurn() {
        this.clearExpression();
        this.generateNumbers();
        this.updateUI();
        
        // Update token positions at the start of each turn
        this.players.forEach((_, index) => this.updateTokenPosition(index));
        
        if (this.players[this.currentPlayer].isComputer) {
            setTimeout(() => this.makeComputerMove(), 1000);
        }
    }

    generateNumbers() {
        this.numbers = [];
        while (this.numbers.length < 4) {
            const num = Math.floor(Math.random() * 9) + 1;
            if (!this.numbers.includes(num)) {
                this.numbers.push(num);
            }
        }
    }

    selectNumber(num) {
        if (this.usedNumbers.size >= 4) return;
        if (this.usedNumbers.has(num)) return;
        
        this.expression.push(num);
        this.usedNumbers.add(num);
        this.updateUI();
    }

    selectOperation(op) {
        if (this.usedOperations.size >= 3) return;
        if (this.usedOperations.has(op)) return;
        if (this.expression.length === 0) return;
        
        this.expression.push(op);
        this.usedOperations.add(op);
        this.updateUI();
    }

    clearExpression() {
        this.expression = [];
        this.usedNumbers.clear();
        this.usedOperations.clear();
        this.updateUI();
    }

    calculateResult() {
        if (this.expression.length < 3) return 0;
        
        // First, handle multiplication and division
        let result = this.expression[0];
        let i = 1;
        
        while (i < this.expression.length) {
            const op = this.expression[i];
            const num = this.expression[i + 1];
            
            if (op === '×' || op === '÷') {
                if (op === '×') {
                    result *= num;
                } else {
                    result = Math.floor(result / num);
                }
                i += 2;
            } else {
                i += 2;
            }
        }
        
        // Then handle addition and subtraction
        i = 1;
        while (i < this.expression.length) {
            const op = this.expression[i];
            const num = this.expression[i + 1];
            
            if (op === '+' || op === '-') {
                if (op === '+') {
                    result += num;
                } else {
                    result -= num;
                }
            }
            i += 2;
        }
        
        return result;
    }

    submitMove() {
        if (this.expression.length < 3) return;
        
        // Check if all numbers were used
        if (this.usedNumbers.size !== 4) {
            alert('You must use all four numbers!');
            return;
        }

        const result = this.calculateResult();
        const currentPosition = this.players[this.currentPlayer].position;
        const newPosition = currentPosition + result;
        
        console.log('Current position:', currentPosition);
        console.log('Move result:', result);
        console.log('New position:', newPosition);
        
        // Check if landed on a town
        let finalPosition = newPosition;
        let jumpedToTown = false;
        for (const town of this.towns) {
            if (newPosition >= town && newPosition < town + 10) {
                finalPosition = town + 10;
                jumpedToTown = true;
                break;
            }
        }
        
        // Check for exact win before clamping
        if (finalPosition === 50) {
            this.players[this.currentPlayer].position = 50;
            this.updateTokenPosition(this.currentPlayer);
            this.gameOver = true;
            alert(`Player ${this.currentPlayer + 1} wins!`);
            return;
        }
        
        // If not exactly 50, clamp the position
        finalPosition = Math.max(0, Math.min(50, finalPosition));
        
        // Update the player's position
        this.players[this.currentPlayer].position = finalPosition;
        this.updateTokenPosition(this.currentPlayer);
        
        // Update the position display
        const positionText = jumpedToTown ? 
            `Position: ${newPosition} → ${finalPosition} (jumped to next town)` :
            `Position: ${finalPosition}`;
        document.querySelector(`#player${this.currentPlayer + 1} .player-position`).textContent = positionText;
        
        // Switch players
        this.currentPlayer = (this.currentPlayer + 1) % 2;
        this.startNewTurn();
    }

    makeComputerMove() {
        // Simple AI: Try to get as close to 50 as possible
        const currentPos = this.players[this.currentPlayer].position;
        const target = 50 - currentPos;
        
        // Try different combinations of numbers and operations
        let bestResult = 0;
        let bestExpression = [];
        
        for (let i = 0; i < this.numbers.length; i++) {
            for (let j = 0; j < this.numbers.length; j++) {
                if (i === j) continue;
                for (let k = 0; k < this.numbers.length; k++) {
                    if (k === i || k === j) continue;
                    for (let l = 0; l < this.numbers.length; l++) {
                        if (l === i || l === j || l === k) continue;
                        
                        const nums = [this.numbers[i], this.numbers[j], this.numbers[k], this.numbers[l]];
                        const ops = ['+', '-', '×', '÷'];
                        
                        // Try different operation combinations
                        for (let op1 of ops) {
                            for (let op2 of ops) {
                                if (op1 === op2) continue;
                                for (let op3 of ops) {
                                    if (op3 === op1 || op3 === op2) continue;
                                    
                                    const expr = [nums[0], op1, nums[1], op2, nums[2], op3, nums[3]];
                                    let result = this.evaluateExpression(expr);
                                    
                                    if (Math.abs(result - target) < Math.abs(bestResult - target)) {
                                        bestResult = result;
                                        bestExpression = expr;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        
        // Apply the best move
        this.expression = bestExpression;
        this.usedNumbers = new Set(bestExpression.filter(x => typeof x === 'number'));
        this.usedOperations = new Set(bestExpression.filter(x => typeof x === 'string'));
        this.updateUI();
        
        setTimeout(() => this.submitMove(), 1000);
    }

    evaluateExpression(expr) {
        let result = expr[0];
        for (let i = 1; i < expr.length; i += 2) {
            const op = expr[i];
            const num = expr[i + 1];
            
            switch (op) {
                case '+': result += num; break;
                case '-': result -= num; break;
                case '×': result *= num; break;
                case '÷': result = Math.floor(result / num); break;
            }
        }
        return result;
    }

    updateTokenPosition(playerIndex) {
        const token = document.getElementById(`token-${playerIndex + 1}`);
        if (!token) {
            console.error(`Token for player ${playerIndex + 1} not found`);
            return;
        }

        const position = this.players[playerIndex].position;
        const square = document.querySelector(`.board-square:nth-child(${position + 1})`);
        if (!square) {
            console.error(`Square at position ${position} not found`);
            return;
        }

        const rect = square.getBoundingClientRect();
        const boardRect = document.getElementById('board-track').getBoundingClientRect();
        
        // Calculate center position of the square
        const centerX = rect.left - boardRect.left + rect.width / 2;
        const centerY = rect.top - boardRect.top + rect.height / 2;
        
        token.style.left = `${centerX}px`;
        token.style.top = `${centerY}px`;
    }

    updateUI() {
        // Update numbers display
        const numbersContainer = document.getElementById('numbers');
        numbersContainer.innerHTML = '';
        this.numbers.forEach(num => {
            const numElement = document.createElement('div');
            numElement.className = `number ${this.usedNumbers.has(num) ? 'used' : ''}`;
            numElement.textContent = num;
            numbersContainer.appendChild(numElement);
        });

        // Update expression display with parentheses
        const expressionElement = document.getElementById('expression');
        let displayExpression = '';
        for (let i = 0; i < this.expression.length; i++) {
            if (i === 0) {
                displayExpression += this.expression[i];
            } else if (i % 2 === 1) { // Operation
                const nextOp = this.expression[i + 2];
                if (this.expression[i] === '×' || this.expression[i] === '÷') {
                    if (i > 1 && (this.expression[i-2] === '+' || this.expression[i-2] === '-')) {
                        displayExpression = `(${displayExpression})`;
                    }
                }
                displayExpression += ` ${this.expression[i]} `;
            } else { // Number
                displayExpression += this.expression[i];
            }
        }
        expressionElement.textContent = displayExpression;

        // Update result display
        const resultElement = document.getElementById('result');
        resultElement.textContent = `Result: ${this.calculateResult()}`;

        // Update operation buttons
        document.querySelectorAll('.op-btn').forEach(btn => {
            btn.disabled = this.usedOperations.has(btn.dataset.op);
        });

        // Update player info
        document.querySelectorAll('.player').forEach((player, index) => {
            player.classList.toggle('active', index === this.currentPlayer);
            const positionElement = player.querySelector('.player-position');
            positionElement.textContent = `Position: ${this.players[index].position}`;
        });
    }
}

// Start the game
new TrainGame(); 