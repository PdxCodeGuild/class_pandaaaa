class BlackJack {
    constructor(mypoints = 0, mycards = [], ) {
        this.mypoints = mypoints;
        this.mycards = mycards;
        this.card_values = {
            'Q': 10,
            'K': 10,
            'J': 10,
            '9': 9,
            '8': 8,
            '7': 7,
            '6': 6,
            '5': 5,
            '4': 4,
            '3': 3,
            '2': 2,
            '1': 1,
        };
        this.usercards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'K', 'Q'];
    }



    //helper function for fill_hand, get random number 0-12
    deal() {
        return parseInt((Math.random() * 100) % 12);
    }



    //deal 3 random cards
    fill_hand() {
        for (let i = 0; i < 3; ++i) {
            this.mycards.push(this.usercards[this.deal()]);
        }
    }



    //calc points
    calc_points() {
        for (let i = 0; i < this.mycards.length; ++i) {
            this.mypoints += parseInt(this.card_values[this.mycards[i]]);
        }
    }



    //return true/false if there is/isn't an ace
    has_ace() {
        if (this.mycards.includes(1)) return true;
        return false;
    }



    //fix aces
    fix_aces() {
        if (this.mypoints <= 11 && this.has_ace()) {
            console.log("Ace Converted.\n");
            this.mypoints += 10;
            return 10;
        }
        return 0;
    }



    //display hand and points to console.
    display_hand() {
        console.log("\n\n");
        console.log("My hand:");
        console.log(this.mycards);
        console.log("\n\n");
        console.log("My points:");
        console.log(this.mypoints);
        console.log("\n\n");
    }



    //display advice to console
    advice_calc() {
        if (this.mypoints < 17) { // less than 17
            console.log("Hit!");
        } else if (this.mypoints < 21) { // greater or equal to 17
            console.log("Stay");
        } else if (this.mypoints == 21) { // exactly 21
            console.log("BlackJack");
        } else { //Over 21
            console.log("Already Busted.");
        }
    }
}


let test_game = function() {
    console.log('WELCOME TO BLACK JACK ADVICE GIVER')
    mygame = new BlackJack();
    mygame.fill_hand();
    mygame.calc_points();
    mygame.fix_aces();
    mygame.display_hand();
    mygame.advice_calc();
}

test_game()