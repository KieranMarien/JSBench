const fs = require('fs');
const csv = require('csv-parser');
const MongoClient = require('mongodb').MongoClient;

// Connection URL and database name
const url = 'mongodb://127.0.0.1/';
const dbName = 'benchmarkdatabase';
const collectionName = 'benchmarkcollection';
async function insertDocuments(docs) {
  const client = new MongoClient(url, { useUnifiedTopology: true });
  try {
    await client.connect();
    const db = client.db(dbName);
    const collection = db.collection(collectionName);
    await collection.insertMany(docs);
  } catch (err) {
    console.log('Error inserting documents:', err);
  } finally {
    client.close();
  }
}

const documents = [];

fs.createReadStream('MOCK_DATA.csv')
  .pipe(csv())
  .on('data', (row) => {
    documents.push(row);
  })
  .on('end', () => {
    insertDocuments(documents);
  });