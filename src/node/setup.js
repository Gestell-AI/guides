import "colors";
import { join } from "node:path";
import { Gestell } from "@gestell/sdk";

const gestell = new Gestell();

async function start() {
  // Create a test organization
  const { id: organizationId } = await gestell.organization.create({
    name: "Test Organization",
    description: "Test Organization",
  });
  console.log("Created new test organization".green.bold, organizationId);

  // Create a test collection
  const { id: collectionId } = await gestell.collection.create({
    organizationId,
    name: "Gestell Guide Collection",
    description: "An example collection created with the Gestell Guide",
    type: "canon",
  });
  console.log("Created new test collection".green.bold, collectionId);

  // Add a category to retrieve all cast members as feature labels
  await gestell.collection.addCategory({
    collectionId,
    name: "Cast Members",
    type: "features",
    instructions: "Retrieve all cast members and their associated actors",
  });

  // Add a category to create a table of all cast members
  await gestell.collection.addCategory({
    collectionId,
    name: "Cast Members Table",
    type: "table",
    instructions:
      "Retrieve all cast members and their associated actors, the table should be structured as:  1. Movie, 2. Name, 3: Actor Name",
  });

  console.log("Created feature and table categories".green.bold);

  // Upload the test documents
  const upload1 = await gestell.document.upload({
    collectionId,
    name: "reservoir.dogs.pdf",
    file: join(process.cwd(), "src", "samples", "reservoir.dogs.pdf"),
  });
  console.log("Uploaded Reservoir Dogs PDF".green.bold, upload1);

  const upload2 = await gestell.document.upload({
    collectionId,
    name: "good.fellas.pdf",
    file: join(process.cwd(), "src", "samples", "good.fellas.pdf"),
  });
  console.log("Uploaded Good Fellas PDF".green.bold, upload2);

  console.log("Uploaded sample documents".green.bold);
  console.log(
    "It may take a few minutes for the documents to process, you can check the status of your collection in the Web UI or retrieving the collection"
  );
}

(async () => start())();
