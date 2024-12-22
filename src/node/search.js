import "colors";
import { Gestell } from "@gestell/sdk";

const gestell = new Gestell();

const prompt = process.argv[2];

async function start() {
  if (!prompt) {
    console.log("Provide an argument to search the collection".yellow.bold);
    return;
  }
  console.log("Running search query:".green.bold, prompt);

  // Retrieve the Gestell Guide Collection
  const collections = await gestell.collection.list({
    search: "Gestell Guide Collection",
  });

  if (collections.result.length === 0) {
    console.log(
      "The Gestell Guide Collection has not been created, run setup.js first"
        .yellow.bold
    );
    return;
  }

  const collectionId = collections.result[0].id;

  // Run the search and display it
  const response = await gestell.query.search({
    collectionId,
    prompt,
    method: "fast",
  });
  console.log(response.result);
}

(async () => start())();
