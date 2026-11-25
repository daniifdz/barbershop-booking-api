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
    

def test_users_table_has_expected_columns():
    table = Base.metadata.tables["users"]

    assert set(table.columns.keys()) == {
        "id",
        "email",
        "password_hash",
        "full_name",
        "phone",
        "role",
        "created_at",
    }


def test_barber_table_has_expected_columns():
    table = Base.metadata.tables["barbers"]

    assert set(table.columns.keys()) == {
        "id",
        "user_id",
        "display_name",
        "active",
    }


def test_appointment_table_has_expected_columns():
    table = Base.metadata.tables["appointments"]

    assert set(table.columns.keys()) == {
        "id",
        "user_id",
        "barber_id",
        "service_id",
        "starts_at",
        "ends_at",
        "status",
    }
    
def test_barber_schedules_table_has_expected_columns():
    table = Base.metadata.tables["barber_schedules"]

    assert set(table.columns.keys()) == {
        "id",
        "barber_id",
        "weekday",
        "start_time",
        "end_time",
}
    
