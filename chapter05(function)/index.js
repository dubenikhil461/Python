function one(a){
    return function(b){
        return a+b
    }
}
// closures + curring
const add5 = one(5);   // a = 5
console.log(add5(10)); // 15 (because a=5 is remembered)

// closures

function makeCounter() {
    let count = 0;
    return function() {
        count++;
        return count;
    }
}
const counter = makeCounter()
console.log(counter())
console.log(counter())