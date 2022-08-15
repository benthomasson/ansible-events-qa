from ansible_events_qa.utils import get_data_path
from ansible_events_qa.utils.cli import CLIRunner


def test_match_condition_sanity():
    """
    Basic test to check that a condition is met with range plugin
    """

    rules = get_data_path("rulesets/test_match_condition.yml")
    result = CLIRunner(rules=rules).run()

    assert result.returncode == 0
    # assert the content of stderr because currently not all errors are captured
    assert not result.stderr.decode()
    assert '"msg": "matched 2"' in result.stdout.decode()
