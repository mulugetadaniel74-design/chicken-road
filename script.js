let currentBet = 20; // መነሻ ውርርድ

function changeBet(amount) {
    currentBet += amount;
    
    // ከ 20 ብር በታች እንዳይወርድ መቆጣጠሪያ
    if (currentBet < 20) {
        currentBet = 20;
        alert("ዝቅተኛው የውርርድ መጠን 20 ብር ነው!");
    }
    
    // በስክሪኑ ላይ እንዲታይ ማድረግ
    document.getElementById('bet-amount').innerText = currentBet;
}
