from nem2 import client
from nem2 import models
from tests import harness
from tests import responses


@harness.mocked_http_test_case({
    'clients': (client.MosaicHTTP, client.AsyncMosaicHTTP),
    'network_type': models.NetworkType.MIJIN_TEST,
    'tests': [
        {
            'name': 'test_get_mosaic',
            'response': responses.MOSAIC_INFO["Ok"],
            'params': [models.MosaicId.create_from_hex('6c699a1517bea955')],
            'method': 'get_mosaic',
            'validation': [
                lambda x: (x.meta_id, '5CC07CBC3A48065F47D6DF80'),
                lambda x: (hex(x.mosaic_id), '0x6c699a1517bea955'),
                lambda x: (x.supply, 8999999998000000),
                lambda x: (x.height, 1),
                lambda x: (x.owner.public_key, "A04335F99D9EE3787528A16C7A302F80D511E9CF71D97D95C2182E0EA75A1EF9"),
                lambda x: (x.revision, 1),
                lambda x: (x.properties.flags, 0x2),
                lambda x: (x.properties.divisibility, 6),
                lambda x: (x.properties.duration, 0),
            ]
        },
        {
            'name': 'test_get_mosaics',
            'response': responses.MOSAICS_INFO["Ok"],
            'params': [[models.MosaicId.create_from_hex('6c699a1517bea955')]],
            'method': 'get_mosaics',
            'validation': [
                lambda x: (len(x), 1),
                lambda x: (x[0].meta_id, '5CC07CBC3A48065F47D6DF80'),
            ]
        },
        # TODO(ahuszagh)
        #   Check if POST /mosaic/names got removed.
        #       It did, but temporarily. Leave the functionality in.
    ],
})
class TestMosaicHTTP(harness.TestCase):
    pass
