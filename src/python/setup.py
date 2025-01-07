import asyncio
import os
from gestell import Gestell

gestell = Gestell()
organization_id = os.getenv("ORGANIZATION_ID")
if not organization_id:
    raise ValueError("ORGANIZATION_ID environment variable is not set")


async def start():
    # Create a test collection
    collection = await gestell.collection.create(
        organization_id=organization_id,
        name="Gestell Guide Collection",
        description="An example collection created with the Gestell Guide",
        type="canon",
    )
    collection_id = collection.id
    print("\033[92m\033[1mCreated new test collection\033[0m", collection_id)

    # Add a category to retrieve all cast members as feature labels
    await gestell.collection.add_category(
        collection_id=collection_id,
        name="Cast Members",
        type="features",
        instructions="Retrieve all cast members and their associated actors",
    )

    # Add a category to create a table of all cast members
    await gestell.collection.add_category(
        collection_id=collection_id,
        name="Cast Members Table",
        type="table",
        instructions="Retrieve all cast members and their associated actors, the table should be structured as:  1. Movie, 2. Name, 3: Actor Name",
    )

    print("\033[92m\033[1mCreated feature and table categories\033[0m")

    # Upload the test documents
    file_path_1 = os.path.join(os.getcwd(), "src", "samples", "reservoir.dogs.pdf")
    upload1 = await gestell.document.upload(
        collection_id=collection_id,
        name="reservoir.dogs.pdf",
        file=file_path_1,
    )
    print("\033[92m\033[1mUploaded Reservoir Dogs PDF\033[0m", upload1)

    file_path_2 = os.path.join(os.getcwd(), "src", "samples", "good.fellas.pdf")
    upload2 = await gestell.document.upload(
        collection_id=collection_id,
        name="good.fellas.pdf",
        file=file_path_2,
    )
    print("\033[92m\033[1mUploaded Good Fellas PDF\033[0m", upload2)

    print("\033[92m\033[1mUploaded sample documents\033[0m")
    print(
        "It may take a few minutes for the documents to process, you can check the status of your collection in the Web UI or retrieving the collection"
    )


if __name__ == "__main__":
    asyncio.run(start())
