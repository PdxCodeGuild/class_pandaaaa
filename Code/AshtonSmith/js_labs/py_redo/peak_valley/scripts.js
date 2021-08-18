const PLAYER_SPEED = 2;



let inputDirection = { x: 0, y: 0 };
let playerPosition = { x: 3, y: 10 }
const myBoard = document.getElementById("board");
const BOARD_HEIGHT = 20;
const BOARD_LENGTH = 20;
let myHeight = 9;
let currCol = 3;
let data = [4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9, 10, 9];
// let data = [2, 3, 4, 5, 6, 5, 4, 5, 6, 7, 8, 9, 10, 9, 8, 6, 8, 9, 10, 9];
// let data = [1, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 4, 5];
// let data = [4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7, 8, 9, 10, 9];

// console.log(data)
// data.splice(0, 1)
// data.push(8)
// console.log(data)
// console.log(data.pop())
// console.log(data.array.splice(0, 2))

let myPeaks = findPeak(data);
let myValleys = findValley(data);

let lastRenderTime = 0;


function main(currentTime) {
    window.requestAnimationFrame(main);
    const secondsSinceLastRender = (currentTime - lastRenderTime) / 1000
    if (secondsSinceLastRender < 1 / PLAYER_SPEED) return;
    lastRenderTime = currentTime;
    console.log(secondsSinceLastRender);
    update();
    draw();
}

window.requestAnimationFrame(main);

function update() {

    processInput();
    // if (playPosition.x)
    // if((x,y) != terrain)
    // console.log(isThereARockAt((playerPosition.x + inputDirection.x), (playerPosition.y + inputDirection.y)));
    // console.log("BOARD : " + myBoard.attributes);
    console.log("PLAYER X: " + data[playerPosition.x]);
    console.log("PLAYER Y: " + playerPosition.y);
    if ((data[playerPosition.x - 1] < (20 - playerPosition.y)) && inputDirection.x == 1) {
        playerPosition.x += inputDirection.x;
    }
    if ((data[playerPosition.x - 1] < (20 - playerPosition.y)) && inputDirection.x == -1) {
        playerPosition.x += inputDirection.x;
    }





    playerPosition.y += inputDirection.y;
    inputDirection = { x: 0, y: 0 };
}

function draw() {
    myBoard.innerHTML = ""
    drawPlayer();
    //terain
    drawWater(myPeaks, myValleys);
    for (let i = 1; i < BOARD_LENGTH + 1; ++i) {
        drawTerrain(BOARD_HEIGHT - data[i - 1], i);
    }


}
///////////////////////////////////////////////////////////////
// input functions
///////////////////////////////////////////////////////////////
function processInput() {
    window.addEventListener('keydown', e => {
        switch (e.key) {
            case 'ArrowUp':
                inputDirection = { x: 0, y: -1 };
                break;
            case 'ArrowLeft':
                inputDirection = { x: -1, y: 0 };
                break;
            case 'ArrowRight':
                inputDirection = { x: 1, y: 0 };
                break;
            case 'ArrowDown':
                inputDirection = { x: 0, y: 1 };
                break;
        }

    })
}

const isThereARockAt = (x, y) => {
    // Loop through rocks, and check if any rock is at the given point.
    const rock = document.getElementsByClassName("terrain")

    // const myBoard = document.getElementById("board");
    // for (let i = 0; i < rock.length; ++i) {
    console.log("ROCK: " + rock[0].getAttribute("data"));

    // }
    // if (rock.x === x && rock.y === y) {
    //     return true;
    // }
    return false;
};
///////////////////////////////////////////////////////////////
// player functions
///////////////////////////////////////////////////////////////
function drawPlayer() {
    const playerElement = document.createElement('div');
    playerElement.style.gridRowStart = playerPosition.y;
    playerElement.style.gridColumnStart = playerPosition.x;
    playerElement.classList.add('player');
    myBoard.appendChild(playerElement);


}




///////////////////////////////////////////////////////////////
// terrain functions
///////////////////////////////////////////////////////////////
// drawTerrain(19, 2)
function drawTerrain(myHeight, currCol) {
    for (let i = BOARD_HEIGHT; i > myHeight; --i) {
        let terrainElement = document.createElement('div');
        terrainElement.style.gridRowStart = i; //y
        terrainElement.style.gridColumnStart = currCol; //x
        if (i == (myHeight + 1)) {
            terrainElement.classList.add('terrain-top');
        } else {
            terrainElement.classList.add('terrain');
        }
        myBoard.appendChild(terrainElement);
    }
}

// DRAW FIRST WATER ONLY:
// waterElement.style.gridRowStart = 20 - data[myPeaks[i]]; //y ... y = 20 - num
// waterElement.style.gridColumnStart = myPeaks[i] + 1; //x

function drawWater(myPeaks, myValleys, ) {
    console.log(myPeaks);
    console.log(myValleys);
    let length = 0;
    for (let i = 0; i < myValleys.length; ++i) {
        length = ((myValleys[i] - myPeaks[i]) * 2) - 1
        console.log(length)
            // for width/length of water
        for (let j = 0; j < length; ++j) {
            let waterElement = document.createElement('div');
            waterElement.style.gridRowStart = 20 - data[myPeaks[i]]; //y ... y = 20 - num
            waterElement.style.gridColumnStart = myPeaks[i] + 1 + j; //x
            waterElement.classList.add('water');
            myBoard.appendChild(waterElement);
            let depth = data[myPeaks[i] - 1] - data[myValleys[i] - 1];
            // for depth
            for (let z = 0; z < depth; ++z) {
                let waterElement = document.createElement('div');
                waterElement.style.gridRowStart = 20 - data[myPeaks[i]] + z; //y ... y = 20 - num
                waterElement.style.gridColumnStart = myPeaks[i] + 1 + j; //x
                waterElement.classList.add('water');
                myBoard.appendChild(waterElement);
            }
        }
    }
}


function findPeak(data) {
    //start at 1 .. 0 can not be a peak
    let my_peaks = [];
    for (let i = 1; i < data.length; ++i) {
        if (data[i + 1] && data[i] > data[i + 1] && data[i] > data[i - 1]) {
            // console.log("PEAK DETECTED AT INDEX: " + i + ". ")
            my_peaks.push(i + 1)
        }
    }
    return my_peaks;
}

function findValley(data) {
    let my_valleys = [];
    for (let i = 1; i < data.length; ++i) {
        if (data[i + 1] && data[i] < data[i + 1] && data[i] < data[i - 1]) {
            // console.log("VALLEY DETECTED AT INDEX: " + i + ". ")
            my_valleys.push(i + 1)
        }
    }
    return my_valleys;
}