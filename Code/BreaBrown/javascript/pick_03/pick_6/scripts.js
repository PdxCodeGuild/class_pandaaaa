let cost = 0;
let winnings = 0;

winnings_dict = { 0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000 };

let number_matches = 0;
let ticket = [];

function create_ticket() {
    ticket = [];
    for (i=0; i<6; i++) {
        let x = Math.floor(Math.random()*99);
        ticket.push(x);
    }
    return ticket;
}

function compare_tickets(winning_ticket, your_ticket) {
    number_matches = 0;
    for (index in your_ticket) {
        if (winning_ticket[index] == your_ticket[index]) {
            number_matches += 1;
        }
    }
    return number_matches;
}

let counter = 0;

while (counter < 100000) {
    cost = cost+2;
    let win_ticket = create_ticket();
    let your_ticket = create_ticket();
    let number_matches = compare_tickets(win_ticket,your_ticket);
    let win_value = winnings_dict[number_matches];
    winnings += win_value;
    counter += 1;
}

let roi = (winnings - cost) / cost;

let output = `You won ${winnings}, and you spent ${cost}, your investment return value was ${roi}`;
console.log(output);