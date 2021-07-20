def _handle_types(value):
    if hasattr(value, "detach"):
        return value.detach().item()
    else:
        return value


class AverageMeter:
    def __init__(self) -> None:
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1) -> None:
        val = _handle_types(val)
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count


class DictAverageMeter:

    def __init__(self,) -> None:
        self.dict_avg = {}

    def update(self, dict_values: dict) -> None:
        for key, item in dict_values.items():
            try:
                self.dict_avg[key].update(item)
            except KeyError:
                self.dict_avg[key] = AverageMeter()
                self.dict_avg[key].update(item)

    def keys(self,):
        return self.dict_avg.keys()

    def __getitem__(self, name):
        self.dict_avg[name]

    def get(self, name, other=None):
        try:
            return self.dict_avg[name]
        except KeyError:
            return self.dict_avg[other]

    @property
    def avg(self,) -> dict:
        return {key: item.avg for key, item in self.dict_avg.items()}
