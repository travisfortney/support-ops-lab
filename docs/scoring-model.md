# Support Health Scoring Model

This is a deliberately small fake-data model. It is meant for testing ideas, not judging real people.

## Signals

- Open tickets add baseline risk.
- Older tickets add risk gradually.
- More replies add risk because long threads often mean confusion or friction.
- Higher priority adds risk.
- Follow-ups due soon add risk unless the ticket is waiting on the customer.
- Low CSAT adds risk; high CSAT gently reduces it.

## Bands

- `green`: under 18
- `yellow`: 18 to 29.9
- `red`: 30 and above

## Useful next experiments

- Add SLA windows by priority.
- Track risk movement over time.
- Compare load by owner without turning it into a leaderboard.
- Add fake quality-review notes for coaching examples.
