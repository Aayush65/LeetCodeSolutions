/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    let isRunning = false;
    let currentRunning;
    
    return async function(...args) {
        clearTimeout(currentRunning);
        currentRunning = await setTimeout(() => fn(...args), t)
    }
    
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */