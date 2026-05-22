import asyncio

async def fetch_data():
    print("Начинаем загрузку...")
    await asyncio.sleep(2)  # Имитация задержки I/O
    print("Данные загружены")
    return {"data": "Пример данных"}

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())
