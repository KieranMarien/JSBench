import { MongoClient } from "https://deno.land/x/mongo/mod.ts";

const url = "mongodb://127.0.0.1/";
const dbName = "benchmarkdatabase";
const collectionName = "benchmarkcollection";

async function main() {
  try {
    const client = new MongoClient();
    await client.connect(url);

    const db = client.database(dbName);
    const collection = db.collection(collectionName);

    const allDocuments = await collection.find({}).limit(100).toArray();

    const femaleDocuments = await collection.find({ gender: "Female" }).toArray();

    client.close();
  } catch (err) {
    console.error("Failed to connect to MongoDB:", err);
  }
}

main();
