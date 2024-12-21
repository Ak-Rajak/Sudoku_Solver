// Create the grid
const grid = document.getElementById('grid');
for (let i = 0; i < 81; i++) {
    const input = document.createElement('input');
    input.type = 'text';
    input.className = 'cell';
    input.maxLength = 1;
    input.addEventListener('input', function (e) {
        if (!/^[1-9]$/.test(e.target.value)) {
            e.target.value = '';
        }
    });
    grid.appendChild(input);
}

function getBoard() {
    const cells = document.getElementsByClassName('cell');
    const board = [];
    for (let i = 0; i < 9; i++) {
        const row = [];
        for (let j = 0; j < 9; j++){
            const value = cells[i * 9 + j].value;
            row.push(value === '' ? 0 : parseInt(value));
        }
        board.push(row);
    }
    return board;
}

async function solveSudoku() {
    const messageEl = document.getElementById('message');
    const cells = document.getElementsByClassName('cell');

    try {
        const response = await fetch('/solve', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ board: getBoard() })
        });

        const data = await response.json();

        if(response.ok){
            const solution = data.solution;
            for (let i = 0; i < 9; i++) {
                for (let j = 0; j < 9; j++) {
                    setTimeout(() => {
                        cells[i * 9 + j].value = solution[i][j];
                    }, (i + j) * 50);
                }
            }
            messageEl.textContent = "Sudoku solved!";
        } else {
            messageEl.textContent = data.error;
        }
    } catch (error) {
        messageEl.textContent = 'An error occurred';
    }
}

function clearGrid() {
    const cells = document.getElementsByClassName('cell');
    for (let cell of cells) {
        cell.value = '';
    }
    document.getElementById('message').textContent = '';
}