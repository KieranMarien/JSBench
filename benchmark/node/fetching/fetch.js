
const prom1 = fetch('http://localhost:9000/products')
const prom2 = fetch('http://localhost:9000/products?q=Laptop')
Promise.all([prom1, prom2])
    .then(results => Promise.all(results.map(r => r.json())))
    .then((res) => {console.log(res)})



