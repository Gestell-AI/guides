import "colors";
import { Gestell } from "@gestell/sdk";

const gestell = new Gestell();

async function start() {
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
  const collection = await gestell.collection.get(collectionId);
  console.log(collection);

  const categories = collection.result.categories;
  let categoryId = "";

  for (const category of categories) {
    if (category.type === "table") {
      categoryId = category.id;
    }
  }

  if (!categoryId) {
    console.log(
      "The Gestell Guide Collection does not have the table category".yellow
        .bold
    );
    return;
  }

  const response = await gestell.query.table({
    collectionId,
    categoryId,
  });
  for (const item of response.result) {
    console.log(item);
  }
}

(async () => start())();
