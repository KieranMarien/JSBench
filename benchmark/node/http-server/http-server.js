const http = require('http');

async function main(){
    const server = http.createServer((req, res) => {
        res.write('Hello World! From Node');
        res.end()
    }).listen(3000)
}

main()