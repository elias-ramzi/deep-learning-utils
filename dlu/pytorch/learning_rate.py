def set_lr(optimizer, lr):
    for param_group in optimizer.param_groups:
        param_group["lr"] = lr


def set_initial_lr(optimizer):
    for param_group in optimizer.param_groups:
        param_group['initial_lr'] = param_group['lr']


def get_lr(optimizer):
    all_lr = {}
    for i, param_group in enumerate(optimizer.param_groups):
        all_lr[i] = param_group['lr']
    return all_lr
