## Relationships

| Relationship               | Cardinality | Foreign key                |
| -------------------------- | ----------- | -------------------------- |
| users - barbers            | 1 to 0..1   | barbers.user_id (unique)   |
| users - appointments       | 1 to N      | appointments.user_id       |
| barbers - barber_schedules | 1 to N      | barber_schedules.barber_id |
| barbers - appointments     | 1 to N      | appointments.barber_id     |
| services - appointments    | 1 to N      | appointments.service_id    |

`appointments` is the join between users, barbers and services. Clients and barbers are related many-to-many through it.
