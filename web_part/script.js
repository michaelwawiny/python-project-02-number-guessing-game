// ==============================
// GAME CONFIGURATION
// ==============================

const difficulties = {

    easy: {
        minimum: 1,
        maximum: 50,
        attempts: 10
    },

    medium: {
        minimum: 1,
        maximum: 100,
        attempts: 7
    },

    hard: {
        minimum: 1,
        maximum: 200,
        attempts: 5
    }

};


// ==============================
// HTML ELEMENTS
// ==============================

const difficultySelect = document.getElementById("difficulty");

const startButton = document.getElementById("start-button");

const guessInput = document.getElementById("guess-input");

const guessButton = document.getElementById("guess-button");

const restartButton = document.getElementById("restart-button");

const message = document.getElementById("message");

const attemptsDisplay = document.getElementById("attempts");

const rangeDisplay = document.getElementById("range");

const gamesPlayedDisplay = document.getElementById("games-played");

const gamesWonDisplay = document.getElementById("games-won");

const totalScoreDisplay = document.getElementById("total-score");


// ==============================
// GAME VARIABLES
// ==============================

let secretNumber;

let remainingAttempts;

let maximumAttempts;

let minimumNumber;

let maximumNumber;

let gameActive = false;

let gameFinished = false;


// ==============================
// STATISTICS
// ==============================

let statistics = loadStatistics();


function loadStatistics() {

    try {

        const saved = localStorage.getItem("guessingGameStats");

        if (!saved) {
            return {
                played: 0,
                won: 0,
                score: 0
            };
        }

        const data = JSON.parse(saved);

        if (
            typeof data.played !== "number" ||
            typeof data.won !== "number" ||
            typeof data.score !== "number"
        ) {
            throw new Error("Invalid statistics");
        }

        return data;

    } catch (error) {

        return {
            played: 0,
            won: 0,
            score: 0
        };

    }

}


function saveStatistics() {

    localStorage.setItem(
        "guessingGameStats",
        JSON.stringify(statistics)
    );

}


function updateStatisticsDisplay() {

    gamesPlayedDisplay.textContent = statistics.played;

    gamesWonDisplay.textContent = statistics.won;

    totalScoreDisplay.textContent = statistics.score;

}


// ==============================
// START GAME
// ==============================

function startGame() {

    const difficulty = difficultySelect.value;

    const settings = difficulties[difficulty];

    minimumNumber = settings.minimum;

    maximumNumber = settings.maximum;

    maximumAttempts = settings.attempts;

    remainingAttempts = maximumAttempts;

    secretNumber = Math.floor(
        Math.random() * (maximumNumber - minimumNumber + 1)
    ) + minimumNumber;

    gameActive = true;

    gameFinished = false;

    rangeDisplay.textContent =
        `${minimumNumber} and ${maximumNumber}`;

    attemptsDisplay.textContent = remainingAttempts;

    message.textContent = "Game started! Enter your first guess.";

    guessInput.disabled = false;

    guessButton.disabled = false;

    guessInput.value = "";

    guessInput.min = minimumNumber;

    guessInput.max = maximumNumber;

    guessInput.focus();

    startButton.textContent = "NEW GAME";

}


// ==============================
// CHECK GUESS
// ==============================

function checkGuess() {

    if (!gameActive || gameFinished) {
        return;
    }

    const guess = Number(guessInput.value);

    if (
        guessInput.value.trim() === "" ||
        !Number.isInteger(guess) ||
        guess < minimumNumber ||
        guess > maximumNumber
    ) {

        message.textContent =
            `Enter a whole number between ${minimumNumber} and ${maximumNumber}.`;

        return;

    }

    remainingAttempts--;

    attemptsDisplay.textContent = remainingAttempts;

    guessInput.value = "";

    if (guess === secretNumber) {

        winGame();

    } else if (guess < secretNumber) {

        message.textContent = "Too LOW! Try a higher number.";

    } else {

        message.textContent = "Too HIGH! Try a lower number.";

    }

    if (guess !== secretNumber && remainingAttempts === 0) {

        loseGame();

    }

    guessInput.focus();

}


// ==============================
// WIN GAME
// ==============================

function winGame() {

    gameFinished = true;

    gameActive = false;

    const score = remainingAttempts * 10 + 20;

    statistics.played++;

    statistics.won++;

    statistics.score += score;

    saveStatistics();

    updateStatisticsDisplay();

    message.textContent =
        `Congratulations! You guessed ${secretNumber}. Your score: ${score}.`;

    disableGame();

}


// ==============================
// LOSE GAME
// ==============================

function loseGame() {

    gameFinished = true;

    gameActive = false;

    statistics.played++;

    saveStatistics();

    updateStatisticsDisplay();

    message.textContent =
        `Game over! The secret number was ${secretNumber}.`;

    disableGame();

}


// ==============================
// DISABLE GAME
// ==============================

function disableGame() {

    guessInput.disabled = true;

    guessButton.disabled = true;

}


// ==============================
// RESTART GAME
// ==============================

function restartGame() {

    gameActive = false;

    gameFinished = false;

    secretNumber = undefined;

    remainingAttempts = 0;

    guessInput.value = "";

    guessInput.disabled = true;

    guessButton.disabled = true;

    attemptsDisplay.textContent = "0";

    message.textContent = "Press START GAME to begin.";

    startButton.textContent = "START GAME";

}


// ==============================
// EVENT LISTENERS
// ==============================

startButton.addEventListener("click", startGame);

guessButton.addEventListener("click", checkGuess);

restartButton.addEventListener("click", restartGame);

guessInput.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {

        checkGuess();

    }

});


// ==============================
// INITIALISE APPLICATION
// ==============================

updateStatisticsDisplay();

restartGame();