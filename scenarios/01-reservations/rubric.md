# Reservations intent rubric

Score the initial intent and its revision. Keep functional results separate.

0 = unresolved contradiction; 1 = relevant but incomplete instruction; 2 = specific supported formulation below; 3 = formulation refined through the stronger evidence below. N/E = not observed. No points for prompt length.

| Dimension | A supported intent at level 2 | Evidence for level 3 |
| --- | --- | --- |
| Problem formulation | Owns incompatible seat promises and defines the repair scope | Separates temporary claim, permanent booking, and original request outcome |
| State modeling | Directs AI to distinguish a seat from a particular hold | Explains why a current seat lookup cannot answer an old hold's request |
| Safety and transitions | Requires live holds plus bookings within capacity and an atomic allocation decision | Predicts both delayed-confirmation and competing-allocation failures |
| Constraints and progress | Uses the given clock, expiry boundary, and durable outcomes | Preserves replay after expiry while recovering capacity without cleanup |
| Falsification and evidence | Specifies a short stale-confirmation history and an observable rejection | Seeks the controlled race or bounded histories rather than only one example |
| Revision and delivery | Updates intent after the adjacent replay case and states remaining failures | Preserves both ownership safety and the already committed promise in one coherent model |

## Concrete checks

- test_old_hold_cannot_confirm_reassigned_seat: old A must not obtain B's seat.
- test_competing_last_seat: both workers see an opportunity; only one promise may commit.
- test_committed_confirmation_replays_after_expiry: a committed promise survives a lost response.
- test_expired_capacity_recovers_without_cleanup: safety must not strand free capacity.
- test_bounded_histories_preserve_capacity: 2,592 length-four histories over two capacities.

An initial instruction such as make it thread-safe gives limited evidence. A meaningful revision identifies which identity or decision boundary was missing, predicts a result, and asks AI to verify the preserved promise.

Return initial intent, revised intent, named executed checks, and limits. A passing suite is functional evidence; it does not automatically provide every intent score.
