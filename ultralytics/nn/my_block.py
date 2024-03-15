"""
自定义block
"""
import torch.nn as nn
import torch.nn.functional as F
from segmentation_models_pytorch.base import modules as md

import os
import timm
import torch


def resnext50_encoder():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    f_dir = os.path.dirname(current_dir)
    base_dir = os.path.dirname(f_dir)
    path = 'pretrain_weights/resnext50_32x4d_a1h-0146ab0a.pth'
    path = os.path.join(base_dir, path)
    m = timm.create_model('resnext50_32x4d', pretrained=False).default_cfg
    m['file'] = path
    model = timm.models.resnext50_32x4d(pretrained=True, pretrained_cfg=m, features_only=True)
    return model


class DecoderBlock(nn.Module):
    def __init__(
            self,
            in_channels,
            skip_channels,
            out_channels,
            use_batchnorm=True,
            attention_type=None,
    ):
        super().__init__()
        self.conv1 = md.Conv2dReLU(
            in_channels + skip_channels,
            out_channels,
            kernel_size=3,
            padding=1,
            use_batchnorm=use_batchnorm,
        )
        self.attention1 = md.Attention(attention_type, in_channels=in_channels + skip_channels)
        self.conv2 = md.Conv2dReLU(
            out_channels,
            out_channels,
            kernel_size=3,
            padding=1,
            use_batchnorm=use_batchnorm,
        )
        self.attention2 = md.Attention(attention_type, in_channels=out_channels)

    def forward(self, inpt_tensor):
        x, skip = inpt_tensor
        x = F.interpolate(x, scale_factor=2, mode="nearest")  # 上采样
        x = torch.cat([x, skip], dim=1)
        x = self.attention1(x)
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.attention2(x)
        return x


class cho_output(nn.Module):
    def __init__(
            self,
            output_id,
    ):
        super().__init__()
        self.output_id = output_id

    def forward(self, x):
        return x[self.output_id]
