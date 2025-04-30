from lm_eval.api.filter import Filter
from lm_eval.api.registry import register_filter


@register_filter("custom")
class CustomFilter(Filter):
    """
    Custom filter that applies a custom, user-defined function to the model responses.
    """

    def __init__(self, **kwargs) -> None:
        self.filter_fn = kwargs.pop("filter_fn")

        super().__init__(**kwargs)

    def apply(self, resps, docs):
        return self.filter_fn(resps, docs)


@register_filter("remove_whitespace")
class RemoveWhitespaceFilter(Filter):
    """
    Filter that removes leading and trailing whitespace from the model responses.
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def apply(self, resps, docs):
        def remove_whitespace(resp):
            return "".join(resp.split())

        return map(lambda r: [remove_whitespace(r)], resps)
