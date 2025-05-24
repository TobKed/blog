from abc import ABC, abstractmethod
from typing import Any


class UrlAnalyserBase(ABC):
    @abstractmethod
    def analyze_url(self, *args, **kwargs) -> Any:
        pass


class UrlAnalyser(UrlAnalyserBase):
    def analyze_url(self, *args, **kwargs):
        pass
