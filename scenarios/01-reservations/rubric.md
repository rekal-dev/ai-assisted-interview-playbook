# Reservations intent rubric

Score the candidate's investigation choices, repair intent, and revision. Keep functional results separate.

0 = unresolved contradiction; 1 = relevant but incomplete instruction; 2 = specific supported formulation below; 3 = formulation refined through the stronger evidence below. N/E = not observed. No points for prompt length.

Ask what caused the incompatible promises, why the candidate chose their approach, and why they accepted or revised AI's proposal. Use short explanations, a walkthrough, or targeted execution as evidence. The anchors illustrate useful decisions; equivalent approaches are welcome. Passing-check count does not set the rating.

| Dimension | A supported intent at level 2 | Evidence for level 3 |
| --- | --- | --- |
| Problem formulation | Explains how the code can make incompatible promises and defines the repair scope | Separates temporary claim, permanent booking, and original request outcome |
| State modeling | Directs AI to distinguish a seat from a particular hold and explains why it matters | Compares deriving availability with maintaining a counter, or another relevant representation choice, and explains the consistency trade-off |
| Safety and transitions | Requires live holds plus bookings within capacity and an atomic allocation decision | Predicts both delayed-confirmation and competing-allocation failures |
| Constraints and progress | Uses the given clock, expiry boundary, and durable outcomes | Preserves replay after expiry while recovering capacity without cleanup |
| Falsification and evidence | Predicts the stale-confirmation result and explains it through the code or a replay | Chooses a related race or replay because it challenges the proposed explanation, and states what it establishes |
| Revision and delivery | Updates intent after the adjacent replay case and states remaining failures | Preserves both ownership safety and the already committed promise in one coherent model |

## Supporting checks: record results separately

- test_old_hold_cannot_confirm_reassigned_seat: old A must not obtain B's seat.
- test_competing_last_seat: both workers see an opportunity; only one promise may commit.
- test_committed_confirmation_replays_after_expiry: a committed promise survives a lost response.
- test_expired_capacity_recovers_without_cleanup: safety must not strand free capacity.
- test_bounded_histories_preserve_capacity: 2,592 length-four histories over two capacities.

An initial instruction such as make it thread-safe gives limited evidence. A meaningful revision identifies which identity or decision boundary was missing, predicts a result, and asks AI to verify the preserved promise.

Return brief investigation notes, repair intent, revised intent, named executed checks, and limits. A passing suite is functional evidence; it does not automatically provide every intent score.
