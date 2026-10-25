from validate_project_bundle import validate


def test_binary_platform_metadata_is_reported_not_read_as_markdown(tmp_path):
    (tmp_path/'._README.md').write_bytes(bytes([0,255,163]))
    result=validate(tmp_path)
    assert not result['passed'] and result['platform_metadata_files']==['._README.md']
