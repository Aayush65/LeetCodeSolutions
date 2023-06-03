/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    const n = init;
    return {
        increment: () => ++init,
        decrement: () => --init,
        reset: () => {
            init = n;
            return init
        },
    }
};


const counter = createCounter(5)
counter.increment(); // 6
counter.reset(); // 5
counter.decrement(); // 4
