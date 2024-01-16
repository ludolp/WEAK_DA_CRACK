###########################################################################
# Created by: Yi-Hsuan Tsai, NEC Labs America, 2019
###########################################################################

from .crack500_s import CRACK500SSegmentation
from .crack500_t import CRACK500TSegmentation
from .crack500crop_s import CRACK500CROPSSegmentation
from .crack500crop_t import CRACK500CROPTSegmentation
from .gaps384_s import GAPS384SSegmentation
from .gaps384_t import GAPS384TSegmentation
from .rissbilder_noncrack_s import RissbildernoncrackSSegmentation
from .rissbilder_noncrack_t import RissbildernoncrackTSegmentation
from .rissbilder_s import RissbilderSSegmentation
from .rissbilder_t import RissbilderTSegmentation
from .cfd_s import CFDSSegmentation
from .cfd_t import CFDTSegmentation
from .deepcrack_s import DeepCrackSSegmentation
from .deepcrack_t import DeepCrackTSegmentation
from .gaps_s import GAPSSSegmentation
from .gaps_t import GAPSTSegmentation
from .cracktree200_s import cracktree200SSegmentation
from .cracktree200_t import cracktree200TSegmentation
from .ganghwa_s import GanghwaSSegmentation
from .ganghwa_t import GanghwaTSegmentation
from .incheon_s import IncheonSSegmentation
from .incheon_t import IncheonTSegmentation
from .gta5 import GTA5Segmentation
from .cityscapes import CityscapesSegmentation

datasets = {
    'crack500_s': CRACK500SSegmentation,
    'crack500_t': CRACK500TSegmentation,
    'crack500crop_s': CRACK500CROPSSegmentation,
    'crack500crop_t': CRACK500CROPTSegmentation,
    'gaps384_s': GAPS384SSegmentation,
    'gaps384_t': GAPS384TSegmentation,
    'rissbilder_noncrack_s': RissbildernoncrackSSegmentation,
    'rissbilder_noncrack_t': RissbildernoncrackTSegmentation,
    'rissbilder_s': RissbilderSSegmentation,
    'rissbilder_t': RissbilderTSegmentation,
    'cfd_s': CFDSSegmentation,
    'cfd_t': CFDTSegmentation,
    'deepcrack_s': DeepCrackSSegmentation,
    'deepcrack_t': DeepCrackTSegmentation,
    'gaps_s': GAPSSSegmentation,
    'gaps_t': GAPSTSegmentation,
    'cracktree200_s': cracktree200SSegmentation,
    'cracktree200_t': cracktree200TSegmentation,
    'ganghwa_s': GanghwaSSegmentation,
    'ganghwa_t': GanghwaTSegmentation,
    'incheon_s': IncheonSSegmentation,
    'incheon_t': IncheonTSegmentation,
    'gta5': GTA5Segmentation,
    'cityscapes': CityscapesSegmentation
}


def get_dataset(name, **kwargs):
    return datasets[name.lower()](name, **kwargs)
