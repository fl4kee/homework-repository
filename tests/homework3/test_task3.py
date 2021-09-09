from homework3.task3 import make_filter

sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {
        "is_dead": True,
        "kind": "parrot",
        "type": "bird",
        "name": "polly"
    },
    {
        "is_dead": False,
        "type": "person",
    }
]


def test_make_filter():
    assert make_filter(name='polly', type='bird').apply(sample_data) == [{
        "is_dead": True,
        "kind": "parrot",
        "type": "bird",
        "name": "polly"
    }]
    assert make_filter(last_name="Gilbert").apply(sample_data) == [{
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    }]
    assert make_filter(type="person").apply(sample_data) == [{
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    }, {
        "is_dead": False,
        "type": "person",
    }]
