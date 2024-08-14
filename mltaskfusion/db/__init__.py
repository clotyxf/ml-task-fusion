from pydantic import BaseModel, Field
from .redis_db import RedisQueue
from .base import _ScikitCompact


class QueueJobModel(BaseModel):
    """队列任务模型"""

    id: str = Field(description="任务ID")
    data: dict = Field(description="任务数据, json 后数据结构")


def queue_client(driver: str = "redis", queue_name="ml-default") -> _ScikitCompact:
    """队列客户端

    Parameters
    ----------
    driver : str, optional
        - `"redis"`: `redis 驱动`

    queue_name : str, optional
        队列名称, by default "ml-default"

    Returns
    -------
    _type_
        _description_
    """

    if driver == "redis":
        pass

    return RedisQueue(queue_name=queue_name)
