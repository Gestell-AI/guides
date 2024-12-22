import asyncio
from gestell import Gestell

gestell = Gestell()


async def start():
    # Retrieve the Gestell Guide Collection
    collections = await gestell.collection.list(search="Gestell Guide Collection")

    if not collections.result:
        print(
            "\033[93m\033[1mThe Gestell Guide Collection has not been created, run setup.js first\033[0m"
        )
        return

    collection_id = collections.result[0].id
    collection = await gestell.collection.get(collection_id)

    categories = collection.result.categories
    category_id = ""

    for category in categories:
        if category.type == "table":
            category_id = category.id

    if not category_id:
        print(
            "\033[93m\033[1mThe Gestell Guide Collection does not have the table category\033[0m"
        )
        return

    response = await gestell.query.table(
        collection_id=collection_id,
        category_id=category_id,
    )
    for item in response.result:
        print(item)


if __name__ == "__main__":
    asyncio.run(start())
