const config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};

let mainScene;
const game = new Phaser.Game(config);
let selectedGem = null;

function updateScore(scene, matches) {
  const pointsPerGem = 10;
  scene.score += matches.length * pointsPerGem;
  scene.scoreText.setText('Score: ' + scene.score);
  // Display the score on the screen
  // You can create a Text object in the create() function to display the score
  console.log(`Score: ${scene.score}`);
}

function randomGemType(scene) {
    return Math.floor(Math.random() * scene.numberOfGems);
}

function createBoard(scene) {
    const board = [];
  
    for (let y = 0; y < scene.boardHeight; y++) {
      const row = [];
      for (let x = 0; x < scene.boardWidth; x++) {
        let gemType;
        do {
          gemType = randomGemType(scene);
        } while (
          (x >= 2 && row[x - 1] === gemType && row[x - 2] === gemType) ||
          (y >= 2 && board[y - 1][x] === gemType && board[y - 2][x] === gemType)
        );
      row.push(gemType);
      }
      board.push(row);
    }
  
    return board;
  }

function printBoard(board) {
  console.log("Board:");
  for (let y = 0; y < board.length; y++) {
    let row = "";
    for (let x = 0; x < board[y].length; x++) {
      row += board[y][x] !== null ? board[y][x].toString().padStart(2, " ") : " -";
      row += " ";
    }
    console.log(row);
  }
}

function drawBoard(scene, board) { 
    const gemSprites = [];
  
    for (let y = 0; y < scene.boardHeight; y++) {
      const row = [];
      for (let x = 0; x < scene.boardWidth; x++) {
        const gemType = board[y][x];
        const gemX = scene.offsetX + x * (scene.gemSize + scene.gemSpacing);
        const gemY = scene.offsetY + y * (scene.gemSize + scene.gemSpacing);
  
        const gem = scene.add.sprite(gemX, gemY, 'gems', gemType);
        gem.setScale(0.5); // Adjust the gem scale as needed
  
        // Add an ID to each gem sprite
        gem.setData('id', { x, y });
  
        // Set the gem sprite as interactive
        gem.setInteractive();
  
        row.push(gem);
      }
      gemSprites.push(row);
    }
  
    return gemSprites;
}

function findMatches(scene) {
  board = scene.board
  const matches = [];

  // Check for horizontal matches
  for (let y = 0; y < scene.boardHeight; y++) {
    for (let x = 0; x < scene.boardWidth - 2; x++) {
      const gemType = board[y][x];

      if (gemType === board[y][x + 1] && gemType === board[y][x + 2]) {
        let matchLength = 3;

        while (x + matchLength < scene.boardWidth && gemType === board[y][x + matchLength]) {
          matchLength++;
        }

        for (let i = 0; i < matchLength; i++) {
          matches.push({ x: x + i, y });
        }

        x += matchLength - 1;
      }
    }
  }

  // Check for vertical matches
  for (let x = 0; x < scene.boardWidth; x++) {
    for (let y = 0; y < scene.boardHeight - 2; y++) {
      const gemType = board[y][x];

      if (gemType === board[y + 1][x] && gemType === board[y + 2][x]) {
        let matchLength = 3;

        while (y + matchLength < scene.boardHeight && gemType === board[y + matchLength][x]) {
          matchLength++;
        }

        for (let i = 0; i < matchLength; i++) {
          matches.push({ x, y: y + i });
        }

        y += matchLength - 1;
      }
    }
  }

  return matches;
}

function removeMatches(scene, matches) {
  var board = scene.board
  const removeDuration = 200;

  for (const match of matches) {
    const { x, y } = match;
    const gem = scene.gemSprites[y][x];

    if (gem) {
      scene.tweens.add({
        targets: gem,
        alpha: 0,
        duration: removeDuration,
        onComplete: () => {
          gem.destroy();
        },
      });
    }
    board[y][x] = null;
    scene.board[y][x] = null;
  }

  return removeDuration;
}

function dropGems(scene) {
  var board = scene.board
  const dropDuration = 200;
  let maxDropTime = 0;

  for (let x = 0; x < scene.boardWidth; x++) {
    let dropDist = 0;

    for (let y = scene.boardHeight - 1; y >= 0; y--) {
      if (board[y][x] === null) {
        dropDist++;
      } else if (dropDist > 0) {
        const gem = scene.gemSprites[y][x];
        const newY = y + dropDist;

        scene.tweens.add({
          targets: gem,
          y: gem.y + dropDist * (scene.gemSize + scene.gemSpacing),
          duration: dropDuration * dropDist,
        });
        
        board[newY][x] = board[y][x];
        board[y][x] = null;

        gem.setData('id', { x:x, y: newY });

        scene.gemSprites[newY][x] = gem;
        scene.gemSprites[y][x] = null;

        maxDropTime = Math.max(maxDropTime, dropDuration * dropDist);
      }
    }

    // Create new gems from above and drop them
    for (let i = 0; i < dropDist; i++) {
      const gemType = randomGemType(scene);
      const gemY = scene.offsetY + (i-dropDist) * (scene.gemSize + scene.gemSpacing);
      const gemX = scene.offsetX + x * (scene.gemSize + scene.gemSpacing);

      const gem = scene.add.sprite(gemX, gemY, 'gems', gemType).setScale(0.5);
      gem.setData('id', { x:x, y: i });

      scene.tweens.add({
        targets: gem,
        y: scene.offsetY + i * (scene.gemSize + scene.gemSpacing),
        duration: dropDuration * (dropDist),
      });

      gem.setInteractive();
      
      board[i][x] = gemType;
      scene.gemSprites[i][x] = gem;

      maxDropTime = Math.max(maxDropTime, dropDuration * (dropDist - i));
    }
  }

  return maxDropTime;
}

function resolveMatches(scene) {
  let matches = findMatches(scene);
  if (matches.length > 0) {
    updateScore(scene, matches);
    const removeTime = removeMatches(scene, matches);
    scene.time.delayedCall(removeTime, () => {
      const dropTime = dropGems(scene);
      scene.time.delayedCall(dropTime, () => resolveMatches(scene));
    });
  }
}

function swapGems(scene, gem1, gem2) {
  const gem1Id = gem1.getData("id");
  const gem2Id = gem2.getData("id");

  // Swap the gems in the board array
  const temp = scene.board[gem1Id.y][gem1Id.x];
  scene.board[gem1Id.y][gem1Id.x] = scene.board[gem2Id.y][gem2Id.x];
  scene.board[gem2Id.y][gem2Id.x] = temp;

  // Swap the gems in the gemSprites array
  const tempSprite = scene.gemSprites[gem1Id.y][gem1Id.x];
  scene.gemSprites[gem1Id.y][gem1Id.x] = scene.gemSprites[gem2Id.y][gem2Id.x];
  scene.gemSprites[gem2Id.y][gem2Id.x] = tempSprite;

  // Update the id data for both gems
  gem1.setData("id", gem2Id);
  gem2.setData("id", gem1Id);

  // Animate the gem swap (use the same duration for both gems)
  const swapDuration = 200;
  const gem1Tween = scene.tweens.add({
    targets: gem1,
    x: gem2.x,
    y: gem2.y,
    duration: swapDuration,
  });

  const gem2Tween = scene.tweens.add({
    targets: gem2,
    x: gem1.x,
    y: gem1.y,
    duration: swapDuration,
  });

  return [gem1Tween, gem2Tween];
}

function onGemClick(pointer, gameObject) {
    const gem = gameObject;
    const scene = gem.scene;
    const gemId = gem.getData('id');
    const gemType = gem.frame.name;
    // If no gem is selected, select the clicked gem
  if (selectedGem === null) {
    selectedGem = gem;
    gem.setTint(0xff0000); // Set a tint color to indicate the selected gem
  } else if (gem === selectedGem) {
    // If the clicked gem is the same as the selected gem, un-choose it
      selectedGem.clearTint();
      selectedGem = null;
    } else {
    // If the clicked gem is adjacent to the selected gem, swap them
    const gemId = gem.getData('id');
    const selectedGemId = selectedGem.getData('id');
    const distanceX = Math.abs(gemId.x - selectedGemId.x);
    const distanceY = Math.abs(gemId.y - selectedGemId.y);

    if ((distanceX === 1 && distanceY === 0) || (distanceX === 0 && distanceY === 1)) {
      const [gem1Tween, gem2Tween] = swapGems(scene, gem, selectedGem);
  
      const handleTweenComplete = () => {
        selectedGem.clearTint();
        const matches = findMatches(scene);
        if (matches.length > 0) {
          resolveMatches(scene);
          selectedGem = null;
        } else {
          const [, swapBackTween] = swapGems(scene, gem, selectedGem);
          swapBackTween.on('complete', () => {
            selectedGem = null;
          });
        }
      };
  
      // Add the onComplete callback to both tweens and increment a counter
      // to ensure both tweens are completed before executing handleTweenComplete
      let completedTweens = 0;
      gem1Tween.on('complete', () => {
        completedTweens++;
        if (completedTweens === 2) {
          handleTweenComplete();
        }
      });
  
      gem2Tween.on('complete', () => {
        completedTweens++;
        if (completedTweens === 2) {
          handleTweenComplete();
        }
      });
    } 
  }
}

function set_constants(scene){
  scene.boardWidth = 8;
  scene.boardHeight = 8;
  scene.numberOfGems = 6;
  scene.gemSize = 64;
  scene.gemSpacing = 2;
  scene.offsetX = (scene.sys.game.config.width - (scene.boardWidth * (scene.gemSize + scene.gemSpacing))) / 2;
  scene.offsetY = (scene.sys.game.config.height - (scene.boardHeight * (scene.gemSize + scene.gemSpacing))) / 2;
}

function preload() {
        this.load.spritesheet('gems', 'assets/gems.png', { frameWidth: 80, frameHeight: 80 });
}

function create() {
    mainScene = this;
    set_constants(this)
    this.board = createBoard(this);
    this.gemSprites = drawBoard(this, this.board);
    this.score = 0;    
    this.input.on('gameobjectdown', onGemClick, this);
    this.scoreBackground = this.add.graphics();
    this.scoreBackground.fillStyle(0xaaaaaa, 1);
    this.scoreBackground.fillRect(10, 530, 250, 50);
    this.scoreText = this.add.text(20, 540, 'Score: 0', { fontSize: '32px', fill: '#FFF' });
}

function update() {
    // Update the game state, such as checking for matches and handling user input
}
