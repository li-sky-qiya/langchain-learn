from pydantic import BaseModel, Field

from agent.my_llm import llm_openai


class Movie(BaseModel):
    """
    电影详情
    """
    title: str = Field(..., description="电影标题")
    year: int = Field(..., description="电影上映年份")
    director: str = Field(..., description="导演")
    rating: float = Field(..., description="评分")

module_with_structure = llm_openai.with_structured_output(Movie,
                                                          # include_raw=True
                                                          ) #include_raw=True表示返回原始数据
response = module_with_structure.invoke("请提供一下电影《霸王别姬》的详细信息")
print(response)