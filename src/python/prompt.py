import asyncio
import sys
from gestell import Gestell

gestell = Gestell()


async def main():
    prompt = sys.argv[1] if len(sys.argv) > 1 else None

    if not prompt:
        print("\033[93m\033[1mProvide an argument to prompt the collection\033[0m")
        return

    print("\033[92m\033[1mRunning prompt:\033[0m", prompt)

    # Retrieve the Gestell Guide Collection
    collections = await gestell.collection.list(search="Gestell Guide Collection")

    if not collections.result:
        print(
            "\033[93m\033[1mThe Gestell Guide Collection has not been created, run setup.py first\033[0m"
        )
        return

    collection_id = collections.result[0].id

    # Run the prompt and pipe it to the terminal
    response = gestell.query.prompt(
        collection_id=collection_id, prompt=prompt, method="fast"
    )

    async for chunk in response:
        print(chunk.decode("utf-8"), end="", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
