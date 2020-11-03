from .base_options import BaseOptions


class WebOptions(BaseOptions):
    """This class includes test options.

    It also includes shared options defined in BaseOptions.
    """

    def initialize(self, parser):
        parser = BaseOptions.initialize(self, parser)  # define shared options
        parser.add_argument('--results_dir', type=str, default='./results/', help='saves results here.')
        parser.add_argument('--aspect_ratio', type=float, default=1.0, help='aspect ratio of result images')
        parser.add_argument('--phase', type=str, default='test', help='train, val, test, etc')
        # Dropout and Batchnorm has different behavior during training and test.
        parser.add_argument('--eval', action='store_true', help='use eval mode during test time.')
        parser.add_argument('--num_test', type=int, default=50, help='how many test images to run')
        # rewrite devalue values
        parser.set_defaults(model='test')
        # To avoid cropping, the load_size should be the same as crop_size
        parser.set_defaults(load_size=parser.get_default('crop_size'))

        self._modify_required(parser, 'dataroot', False)
        parser.set_defaults(dataroot="datasets/artwork-new/testA")
        parser.set_defaults(gpu_ids='-1')
        self.isTrain = False
        
        # self.dataroot = "datasets/artwork-new/testA"
        return parser

    def _modify_required(self, parser, dest, required):
        for action in parser._actions:
            if action.dest == dest:
                action.required = required
                return
        else:
            raise AssertionError('argument {} not found'.format(dest))
