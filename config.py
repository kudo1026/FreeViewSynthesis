from pathlib import Path
import socket
import platform
import getpass

HOSTNAME = socket.gethostname()
PLATFORM = platform.system()
USER = getpass.getuser()

train_device = "cuda:0"
eval_device = "cuda:0"
dtu_root = None
tat_root = None
colmap_bin_path = None
lpips_root = None


tat_train_sets = [
    "ibr3d_tat/training/Barn",
    "ibr3d_tat/training/Caterpillar",
    "ibr3d_tat/training/Church",
    "ibr3d_tat/training/Courthouse",
    "ibr3d_tat/training/Ignatius",
    "ibr3d_tat/training/Meetingroom",
    "ibr3d_tat/intermediate/Family",
    "ibr3d_tat/intermediate/Francis",
    "ibr3d_tat/intermediate/Horse",
    "ibr3d_tat/intermediate/Lighthouse",
    "ibr3d_tat/intermediate/Panther",
    "ibr3d_tat/advanced/Auditorium",
    "ibr3d_tat/advanced/Ballroom",
    "ibr3d_tat/advanced/Museum",
    "ibr3d_tat/advanced/Temple",
    "ibr3d_tat/advanced/Courtroom",
    "ibr3d_tat/advanced/Palace",
    "ibr3d_tat/training/Truck",
    "ibr3d_tat/intermediate/M60",
    "ibr3d_tat/intermediate/Playground",
    "ibr3d_tat/intermediate/Train",
    "hall_datasets/gerrard_hall",
    "hall_datasets/graham_hall_exterior",
    "hall_datasets/graham_hall_interior",
    "hall_datasets/person_hall"
]

tat_eval_sets = [
    "hall_datasets/south_building"
]

# tat_eval_sets = [
#     "training/Truck",
#     "intermediate/M60",
#     "intermediate/Playground",
#     "intermediate/Train",
# ]

# tat_train_sets = [
#     "gerrard_hall",
#     "graham_hall_exterior",
#     "graham_hall_interior",
#     "person_hall"
# ]


# fmt: off
tat_eval_tracks = {}
tat_eval_tracks['training/Truck'] = [172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196]
tat_eval_tracks['intermediate/M60'] = [94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129]
tat_eval_tracks['intermediate/Playground'] = [221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252]
tat_eval_tracks['intermediate/Train'] = [174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248]

dtu_eval_sets = [65, 106, 118]

dtu_interpolation_ind = [13, 14, 15, 23, 24, 25]
dtu_extrapolation_ind = [0, 4, 38, 48]
dtu_source_ind = [idx for idx in range(49) if idx not in dtu_interpolation_ind + dtu_extrapolation_ind]
# fmt: on


lpips_root = None

# waypoint dataset evaluation
# the parents of these paths must contain proper tat-style dataset
waypoint_eval_sets = [
    "hall_datasets/south_building/dense/ibr3d_test"
]


# TODO: adjust path
# tat_root = Path("/path/to/colmap_tat/")
tat_root = Path("/home/kudo/external_disk/FVS_data")
