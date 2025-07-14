from fastmcp import FastMCP
import asyncio

mcp = FastMCP("server")

@mcp.tool
async def weather(local: str) -> str:
    """
    현재 온도 조회
    :param local: 지역명 (python_weather 라이브러리 사용
        ㄴ 지역명은 python_weather 라이브러리에서 받을 수 있는 명칭을 입력해야합니다.
            예: ("Seoul", "New York")
    """
    import python_weather
    async with python_weather.Client() as client:
        forecast = await client.get(local)
        return f"일자: {forecast.daily_forecasts[0].date} 온도: 썹시{forecast.daily_forecasts[0].temperature}도"

if __name__ == "__main__":
    mcp.run(host="127.0.0.1", port=3000, transport='http')