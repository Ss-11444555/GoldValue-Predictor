# Activity List – Week 09
Project: GoldValue-Predictor

## Activity Definitions

| Activity ID | Activity Name | Duration (days) |
|------------|----------------|-----------------|
| A | Requirements analysis | 3 |
| B | Data collection | 5 |
| C | Data preprocessing | 4 |
| D | Feature engineering | 3 |
| E | Model training | 6 |
| F | Testing & validation | 4 |
| G | Documentation | 2 |
| H | Final submission | 1 |

## Activity Dependencies

| Activity | Predecessor(s) |
|---------|---------------|
| A | — |
| B | A |
| C | B |
| D | C |
| E | D |
| F | E |
| G | F |
| H | G |


## Critical Path (AoA)

- Critical Path: A → B → C → D → E → F → G → H
- Project Duration: 28 days


## Schedule Crashing Analysis

| Activity | Original Duration | Crashed Duration | Impact |
|---------|------------------|------------------|--------|
| E (Model training) | 6 days | 4 days | Extra cloud computing resources |
| F (Testing & validation) | 4 days | 3 days | Additional testing effort |

## Crashing Results

- New project duration: 25 days
- New critical path: A → B → C → D → E → F → G → H
- Crashing was effective because the reduced activities are on the critical path.

