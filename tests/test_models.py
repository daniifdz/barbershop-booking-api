from app.models import Base


def test_services_table_has_expected_columns():
    table = Base.metadata.tables["services"]

    assert set(table.columns.keys()) == {
        "id",
        "name",
        "duration_minutes",
        "price",
        "active",
    }