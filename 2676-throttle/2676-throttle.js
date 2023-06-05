/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function(fn, t) {
    let isThrottled = false;
    let nextArgs;
    
    function helper() {
        if (!isThrottled && nextArgs) {
            fn(...nextArgs);
            isThrottled = true;
            nextArgs = undefined;
            setTimeout(() => {
                isThrottled = false;
                helper();
            }, t)
        }
    }
    
    return function throttled(...args) {
        nextArgs = args;
        helper();
    }
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */