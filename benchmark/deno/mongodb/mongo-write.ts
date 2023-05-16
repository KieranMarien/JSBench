import { MongoClient } from "https://deno.land/x/mongo/mod.ts";

async function main() {
  const uri = "mongodb://127.0.0.1/"; // Update with your MongoDB connection URI
  const client = new MongoClient();

  try {
    await client.connect(uri);

    const database = client.database("node");
    const collection = database.collection("students");

    // Insert a student
    await collection.insertOne({ id: 1, name: "John", age: 6, grade: 1 });

    const arr = [];
    for (let i = 0; i < 10; i++) {
      arr.push({ id: i, name: i + "name", age: i, grade: i });
    }
    await collection.insertMany(arr);

    // Drop the collection (table)
    await collection.drop();
  } catch (error) {
    console.error("Error:", error);
  } finally {
    await client.close();
  }
}

main();
