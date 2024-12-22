import asyncio
import sys
from gestell import Gestell

gestell = Gestell()


async def main():
    if len(sys.argv) < 2:
        print("\033[33m\033[1mProvide an argument to search the collection\033[0m")
        return

    prompt = sys.argv[1]
    print("\033[32m\033[1mRunning search query:\033[0m", prompt)

    # Retrieve the Gestell Guide Collection
    collections = await gestell.collection.list(search="Gestell Guide Collection")

    if not collections.result:
        print(
            "\033[33m\033[1mThe Gestell Guide Collection has not been created, run setup.js first\033[0m"
        )
        return

    collection_id = collections.result[0].id

    # Run the search and display it
    response = await gestell.query.search(
        collection_id=collection_id, prompt=prompt, method="fast"
    )
    print(response.result)


if __name__ == "__main__":
    asyncio.run(main())
