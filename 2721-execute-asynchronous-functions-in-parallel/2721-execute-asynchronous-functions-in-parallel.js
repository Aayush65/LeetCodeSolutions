/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = async function(functions) {
    return new Promise((resolve, reject) => {
        const ans = Array(functions.length);
        let count = 0;
        for (const i in functions)
            functions[i]()
                .then((res) => {
                    ans[i] = res;
                    count ++;
                    if (count === functions.length)
                        resolve(ans);
                })
                .catch((err) => reject(err));
    });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */