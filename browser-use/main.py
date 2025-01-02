import asyncio

from browser_use import Agent
from langchain_openai import ChatOpenAI


async def main():
    agent = Agent(
        task="""
あなたは価格監視のエージェントです。
与えられたURLから商品の監視をしてください
対象商品は: ロイヤルカナン 犬用 消化器サポート 低脂肪 小型犬用S 3kgx1
- Sundrug-online url: https://sundrug-online.com/products/3182550925792
- Rakuten url: https://item.rakuten.co.jp/sundrug/3182550925792/
- yodobashi url: https://www.yodobashi.com/product/100000001008730001/

下記の形式でデータを教えてほしい
- 価格
- 送料(なけれな0円)
- クーポン(なけれな0円)
- ポイント(なけれな0円)
- ショップ名
""",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    print(result)


asyncio.run(main())
