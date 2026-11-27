from sqlalchemy import inspect


def test_migrations_create_all_tables(engine):
    tables = set(inspect(engine).get_table_names())

    assert {
        "users",
        "services",
        "barbers",
        "barber_schedules",
        "appointments",
    } <= tables