import torch
import torch.nn as nn


def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)


def freeze_batch_norm(model):
    for module in filter(lambda m: type(m) == nn.BatchNorm2d, model.modules()):
        module.eval()
        module.train = lambda _: None
    return model


def freeze_pos_embedding(net):
    net.pos_embed.requires_grad_(False)
    return net


def get_gradient_norm(net):
    if torch.cuda.device_count() > 1:
        net = net.module

    if hasattr(net, 'fc'):
        final_layer = net.fc

    elif hasattr(net, 'blocks'):
        final_layer = net.blocks[-1].mlp.fc2

    return torch.norm(list(final_layer.parameters())[0].grad, 2)
