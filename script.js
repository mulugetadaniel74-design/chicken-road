let chicken = document.getElementById('chicken');
let gameArea = document.getElementById('game-area');
let scoreDisplay = document.getElementById('score-value');
let y = 20; let x = 50; let score = 0;

function move(dir) {
    if (dir === 'up') y += 30;
    if (dir === 'down' && y > 20) y -= 30;
    if (dir === 'left' && x > 5) x -= 10;
    if (dir === 'right' && x < 90) x += 10;
    chicken.style.bottom = y + 'px';
    chicken.style.left = x + '%';
    score += 1;
    scoreDisplay.innerText = score;
}

function createCar() {
    let car = document.createElement('div');
    car.innerHTML = "🚗";
    car.style.position = "absolute";
    car.style.fontSize = "40px";
    car.style.left = "-50px";
    car.style.bottom = (Math.floor(Math.random() * 5) * 60 + 100) + "px";
    gameArea.appendChild(car);

    let pos = -50;
    let interval = setInterval(() => {
        pos += 5;
        car.style.left = pos + "px";
        
        let cRect = chicken.getBoundingClientRect();
        let carRect = car.getBoundingClientRect();
        if (!(cRect.right < carRect.left || cRect.left > carRect.right || cRect.bottom < carRect.top || cRect.top > carRect.bottom)) {
            alert("ተገጨህ! ነጥብህ: " + score);
            location.reload();
        }

        if (pos > window.innerWidth) {
            clearInterval(interval);
            car.remove();
        }
    }, 30);
}
setInterval(createCar, 1500);
