###########################################################################
# Created by: Yi-Hsuan Tsai, NEC Labs America, 2019
###########################################################################

from .deeplab_multi import get_deeplab_multi 
from .convnext import get_convnext_tiny, get_convnext_small, get_convnext_base, get_convnext_large, get_convnext_xlarge
from .discriminator import get_discriminator, get_classwise_discriminator


def get_segmentation_model(name, **kwargs):
    models = {
        'deeplab': get_deeplab_multi,
        'convnext_tiny': get_convnext_tiny,
        'convnext_small': get_convnext_small,
        'convnext_base': get_convnext_base,
        'convnext_large': get_convnext_large,
        'convnext_xlarge': get_convnext_xlarge
    }
    return models[name.lower()](**kwargs)


def get_discriminator_model(name, **kwargs):
    if name == 'discriminator':
        models = {'discriminator': get_discriminator}
    if name == 'cw_discriminator':
        models = {'cw_discriminator': get_classwise_discriminator}
    return models[name.lower()](**kwargs)
