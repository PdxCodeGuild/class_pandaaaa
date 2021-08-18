// version 1

let num_list = [5, 0, 8, 3, 4, 1, 6];

function avg_nums(x) {
    let s = 0;
    console.log(x);
    for (i in x) {
        s += x[i];
        console.log(i);
    };
    console.log(s);
    answer = s / x.length;
    return answer;
    };
console.log(avg_nums(num_list));



// version 2

function list_popuation() {
    let l = [];
    while (true) {
        let ui = prompt('Enter a number to add to the list or "done" to exit: ');
        if (ui = 'done') {
            break;
        };
        if (!ui.isNumeric()) {
            console.log('Error, please enter a number!');
            continue;
        }
        else {
            l.push(int(ui));
        }
        }
    }

function run() {
    let l = list_popuation();
        let output = avg_nums(1);
        console.log('The average of the numbers you entered is: {output}');
};