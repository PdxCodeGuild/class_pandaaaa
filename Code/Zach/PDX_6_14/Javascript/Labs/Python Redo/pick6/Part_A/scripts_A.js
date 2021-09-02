//Zach Watts
//Pick_6 Javascript Redo


//PART A
let numberizer = function(){
    return Math.floor(Math.random()*99)
}

let pick6 = function(){
    let the_6 = []
    for (let i=0; i<6; i++){
        the_6.push(numberizer())
    }
    return the_6
}

// while (the_6.length < 6){
//     the_6.push(numberizer())}

let num_matches = function(winning6, ticket){
    let matches = 0
    if (winning6[0] == ticket[0]){
        matches += 1}
    else if (winning6[1] == ticket[1]){
        matches += 1}
    else if (winning6[2] == ticket[2]){
        matches += 1}
    else if (winning6[3] == ticket[3]){
        matches += 1}
    else if (winning6[4] == ticket[4]){
        matches += 1}
    else if (winning6[5] == ticket[5]){
        matches += 1}
    return matches
}

let winnings = function(winning6, ticket){
    if (num_matches(winning6, ticket) == 0){
        return 0}
    else if (num_matches(winning6, ticket) == 1){
        return 4}
    else if (num_matches(winning6, ticket) == 2){
        return 7}
    else if (num_matches(winning6, ticket) == 3){
        return 100}
    else if (num_matches(winning6, ticket) == 4){
        return 50000}
    else if (num_matches(winning6, ticket) == 5){
        return 1000000}
    else if (num_matches(winning6, ticket) == 6){
        return 25000000}}

let el_accountador = function(){
    let balance = 0
    let winning6 = pick6()
    let tix = []
    let earnings = 0
    let expenses = 0
    for (let i=0; i<100; ++i){
        tix.push(pick6())
        console.log(tix)
        balance -= 2
        expenses -= 2}
    for (i in tix){
        balance += winnings(winning6, tix[i])
        earnings += winnings(winning6, tix[i])}
    roi = (earnings - expenses)/expenses
    alert(`Your current balance is $${balance}, your current Return\n
    on Investment is $${roi}, your Earnings are $${earnings}, your Expenses are $${expenses}`)
    return balance}

el_accountador()
