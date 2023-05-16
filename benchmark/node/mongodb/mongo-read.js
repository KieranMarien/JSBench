const { MongoClient } = require('mongodb');

const url = 'mongodb://127.0.0.1/';
const dbName = 'benchmarkdatabase';
const collectionName = 'benchmarkcollection';

async function main() {
  try {
    const client = await MongoClient.connect(url);
    const db = client.db(dbName);
    const collection = db.collection(collectionName);

    const allDocuments = await collection.find({}).limit(100).toArray();

    const femaleDocuments = await collection.find({ gender: 'Female' }).toArray();

    await client.close();
  } catch (err) {
    console.error('Failed to connect to MongoDB:', err);
  }
}
main();
