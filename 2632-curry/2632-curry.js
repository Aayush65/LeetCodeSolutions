/**
 * @param {Function} fn
 * @return {Function}
 */
var curry = function(fn) {
    let completeArgs = [];
    return function curried(...args) {
        completeArgs = [...completeArgs, ...args];
        if (fn.length == completeArgs.length){
            return fn(...completeArgs);
        }
        return curried;
    };
};

/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */
