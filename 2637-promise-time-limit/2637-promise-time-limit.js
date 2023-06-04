/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
	return async function(...args) {
        return new Promise(async (resolve, reject) => {
            const timeout = setTimeout(() => reject("Time Limit Exceeded"), t);
            try {
                const response = await fn(...args);
                resolve(response);
            } catch(err) {
                reject(err)
            }
            
                // .then((res) => resolve(res))
                // .catch((err) => reject(err))
                // .finally(() => clearTimeout(timeout));
        })
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */