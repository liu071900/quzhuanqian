from typing import Dict,Any


class sessionData():
    """
        session 类拓展用户信息
    """
    def __init__(self):
        
        self._map:Dict[str,Any] = dict()

    def __setattr__(self,key:str,value:Any):
        self._map.update(key=value)
    
    def __getattr__(self,key) ->Any:
        return self._map.get(key,None)

    