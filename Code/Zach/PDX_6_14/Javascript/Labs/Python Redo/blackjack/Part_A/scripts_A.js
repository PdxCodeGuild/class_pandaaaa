//Zach Watts
//Blackjack Javascript Redo


card_values = {
    'K':10,
    'Q':10,
    'J':10,
    '10':10,
    '9':9,
    '8':8,
    '7':7,
    '6':6,
    '5':5,
    '4':4,
    '3':3,
    '2':2,
    '1':1
}
let usercards = ['2','3','4','5','6','7','8','9','J','Q','K','A'];
let hand = [];

let deal = function(){
    return usercards[Math.floor(Math.random()*usercards.length)]
};

while (hand.length < 3){
    hand.push(deal())}

let scoring = function(){
    let aces_removed = []
    let ace_count = 0
    let score = 0
    for (let i=0; i<hand.length; i++){
        if (hand[i] == 'A'){
            hand.splice(i, 1)
            ace_count += 1}
        aces_removed = hand
    }
    for (card in aces_removed){
        score += card_values[aces_removed[card]]
    }
    console.log(`score = ${score}`)
    console.log(`aces removed = ${aces_removed}`)
    console.log(`hand = ${hand}`)
    if (ace_count == 3){
        score = 13
    }
    else if(ace_count == 2 &&  score == 10){
        score = 12
    }
    else if(ace_count == 2 && score < 9){
        score += 12}
    if (ace_count == 1 && score >= 11){
        score += 1}    
    else if (ace_count == 1 && score <= 10){
        score += 11}
    return score
}

let user_feedback = function(score){
    if (score < 17){
        alert(`${score} Hit!`)
    }
    else if (17 <= score && score < 21){
        alert(`${score} Stay`)
    }
    else if (score == 21) {
        alert(`${score} Blackjack!`)
    }
    else{
        alert(`${score} Already busted!`)
    }
}

alert(`you've been dealt: ${hand}`)
user_feedback(scoring())